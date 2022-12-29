from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
oauth = OAuth2(None, None, from_file='oauth2.json')


if not oauth.token_is_valid():
    oauth.refresh_access_token()

gm = yfa.Game(oauth, 'nhl')

leagues = gm.league_ids()

league = [ id for id in leagues if '50662' in id][0]
print(league)
lg = gm.to_league(league)

teamkey = lg.team_key()

team = lg.to_team(teamkey)
print(team.roster())