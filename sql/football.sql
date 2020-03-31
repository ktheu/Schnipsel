-- Modify it to show the matchid and player name for all goals scored by Germany. 
-- To identify German players, check for: teamid = 'GER'

SELECT g.matchid, g.player from goal g 
join eteam e on e.id = g.teamid
  WHERE e.id = 'GER'


-- Show id, stadium, team1, team2 for just game 1012
SELECT id,stadium,team1,team2
  FROM game
where id = '1012'