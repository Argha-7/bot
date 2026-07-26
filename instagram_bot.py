"""
==============================================================================
Instagram Auto Comment Bot — Instagrapi Based
GitHub Actions pe chalega — Computer off hone pe bhi!
==============================================================================
Setup:
  1. GitHub pe ek naya repository banao
  2. Is puri folder ko push karo
  3. GitHub Secrets mein add karo:
       INSTAGRAM_USERNAME  → aapka username
       INSTAGRAM_PASSWORD  → aapka password
       POST_URL            → jis post pe comment karna hai (optional)
  4. GitHub Actions khud har 10 minute mein run karega!
==============================================================================
"""

import os
import sys
import logging
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ChallengeRequired

# ==============================================================================
# Logging Setup
# ==============================================================================
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# ==============================================================================
# Settings — GitHub Secrets se automatically aayenge
# ==============================================================================
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME", "")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD", "")

# Jis post pe comment karna hai uska URL
POST_URL = os.environ.get(
    "POST_URL",
    "https://www.instagram.com/p/XXXXXXXXXXXXXXX/"   # ← Yahan apna post URL daalo
)

# Jo comment post hoga — GitHub Secret "COMMENT_TEXT" se override kar sakte ho
COMMENT_TEXT = os.environ.get(
    "COMMENT_TEXT",
    (
        "Respected PM @narendramodi ji, please ek India ek cutoff policy laiye. "
        "Agar koi student general exam mein 90 marks laata hai aur use seat nahi milti, "
        "jabki 40 marks wale ko reservation ki wajah se milti hai — yeh talent ke saath anyay hai. "
        "Ek nation, ek merit, ek cutoff! Hum sabhi chahte hain ki mehnat ka sahi fal mile. "
        "\U0001f1ee\U0001f1f3 #OneNationOneMerit #OneNationOneCutoff"
    )
)


def get_media_id_from_url(client: Client, url: str) -> str:
    """Post URL se media ID nikalo."""
    try:
        parts = url.rstrip("/").split("/")
        shortcode = parts[-1] if parts[-1] else parts[-2]
        media_id = client.media_pk_from_code(shortcode)
        logger.info(f"Media ID mila: {media_id}")
        return media_id
    except Exception as e:
        logger.error(f"Media ID nikalne mein error: {e}")
        raise


def login(client: Client) -> bool:
    """Instagram pe login karo."""
    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
        logger.error("❌ INSTAGRAM_USERNAME ya INSTAGRAM_PASSWORD set nahi hai!")
        logger.error("   GitHub Secrets mein add karo (Settings > Secrets > Actions).")
        return False

    logger.info(f"Instagram login kar raha hoon: @{INSTAGRAM_USERNAME}")

    try:
        client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        logger.info("✅ Login successful!")
        return True

    except ChallengeRequired:
        logger.error("❌ Instagram ne challenge maanga (2FA/Captcha). Ek baar manually login karo.")
        return False
    except LoginRequired:
        logger.error("❌ Login failed. Username/Password check karo.")
        return False
    except Exception as e:
        logger.error(f"❌ Login error: {e}")
        return False


def post_comment() -> bool:
    """Instagram post pe comment karo."""
    client = Client()
    client.delay_range = [2, 5]   # Human-like delay for bot detection avoidance

    if not login(client):
        return False

    try:
        logger.info(f"Post URL: {POST_URL}")
        media_id = get_media_id_from_url(client, POST_URL)

        logger.info(f"Comment post kar raha hoon...")
        logger.info(f"Text: {COMMENT_TEXT}")

        result = client.media_comment(media_id, COMMENT_TEXT)

        if result:
            logger.info(f"✅ Comment successfully post hua!")
            logger.info(f"   Comment ID: {result.pk}")
            return True
        else:
            logger.error("❌ Comment post nahi hua.")
            return False

    except Exception as e:
        logger.error(f"❌ Comment error: {e}")
        return False
    finally:
        try:
            client.logout()
        except Exception:
            pass
        logger.info("Logged out.")


if __name__ == "__main__":
    logger.info("=" * 55)
    logger.info("  Instagram Comment Bot — GitHub Actions Run")
    logger.info("=" * 55)
    logger.info(f"  Account : @{INSTAGRAM_USERNAME}")
    logger.info(f"  Post    : {POST_URL}")
    logger.info("=" * 55)

    success = post_comment()
    sys.exit(0 if success else 1)
