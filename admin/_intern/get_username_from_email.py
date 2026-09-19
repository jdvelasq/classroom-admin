from admin._intern.gh import GhError, run_gh_json


def get_username_from_email(email):
    """Resolve a GitHub username from a public profile email; None if not found or on API failure."""

    try:
        result = run_gh_json(["api", f"search/users?q={email}+in:email"])
    except GhError as error:
        print(f"  gh api error for {email}: {error}")
        return None

    items = result["items"]

    if not items:
        return None

    return items[0]["login"]
