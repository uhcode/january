from quart import (
    Quart,
    render_template,
    jsonify,
    Blueprint,
    redirect
)

api = Blueprint('api', __name__)

# Home page.
@api.route('/')
async def home():
    """
    The home page to January and it's services.
    """

    return await render_template('index.html')

# Terms of service.
@api.route('/terms')
async def terms():
    """
    The terms of service for January.
    """

    return await render_template('terms.html')

# Privacy policy.
@api.route('/privacy')
async def privacy():
    """
    The privacy policy for January.
    """

    return await render_template('privacy.html')

# Github redirect.
@api.route('/github')
async def github():
    """
    The GitHub repository for January.
    """

    return redirect('https://github.com/uhcode/january')