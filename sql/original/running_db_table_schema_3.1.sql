select runnerid,firstname,lastname,grade,time,pace,racename,date,coursedistance,coursename,raceid
from result natural join race natural join course 
	natural join competitor natural join runner 
	natural join gender natural join racename
where courseid=1 and genderid=3
-- where coursename="toro park"
order by time asc;



select runnerid,firstname,lastname,grade,time,pace,racename,date,coursedistance,coursename,raceid
from result natural join race natural join course 
	natural join competitor natural join runner 
	natural join gender natural join racename
where time in (
	select min(time) 
	from result natural join race natural join course 
		natural join competitor natural join runner
	where courseid=1
	group by runnerid
) and courseid=1
order by time asc;



select firstname,lastname,grade,time,pace,date,coursedistance,racename,coursename
from result natural join race natural join course 
	natural join competitor natural join runner 
	natural join gender natural join racename
where runnerid=1 
-- where firstname="girmay"
order by date asc;


select firstname,lastname,grade,time,pace,date,coursedistance,racename,coursename
from result natural join race natural join course 
	natural join competitor natural join runner 
	natural join gender natural join racename
-- where runnerid=1 
-- where firstname="girmay"
where coursename like '%toro%'
order by pace asc;


select firstname,lastname,min(time) as time,coursedistance,coursename
from result natural join race natural join course 
	natural join competitor natural join runner
where coursename='Crystal Springs' and coursedistance=2.95 and grade=9
group by runnerid
order by time asc;

select firstname,lastname,min(time) as time,coursedistance,coursename
from result natural join race natural join course 
	natural join competitor natural join runner
where coursename='Crystal Springs' and coursedistance=2.95 and grade=10
group by runnerid
order by time asc;

select firstname,lastname,min(time) as time,coursedistance,coursename
from result natural join race natural join course 
	natural join competitor natural join runner
where coursename='Crystal Springs' and coursedistance=2.95 and grade=11
group by runnerid
order by time asc;

select firstname,lastname,min(time) as time,coursedistance,coursename
from result natural join race natural join course 
	natural join competitor natural join runner
where coursename='Crystal Springs' and coursedistance=2.95 and grade=12
group by runnerid
order by time asc;

select firstname,lastname,grade,time,pace,date,coursedistance,racename,coursename
from result natural join race natural join course 
	natural join competitor natural join runner 
	natural join gender natural join racename
where genderid=3
order by pace asc
limit 100;


-- how many years a runner has ran
-- 4: 30, 3: 66, 2: 91, 1: 188
select r.runnerid,firstname,lastname,starthsxcyear,endhsxcyear,gender,yrs
from runner r natural join gender 
left join (
select runnerid,count(runnerid) yrs from competitor group by runnerid
) s on r.runnerid = s.runnerid
where yrs=4
order by yrs desc, starthsxcyear asc, runnerid asc; 


-- GET TOP 25 INDIVIDUAL TIMES FOR A COURSE/GENDER
-- third, add myrank number column
SELECT @rownum := @rownum + 1 AS myrank, t.* 
from (
	-- second, join the best times with runner information and sort by best time
	select distinct firstname,lastname,result.time,pace,year,grade
	from result natural join competitor natural join runner natural join gender natural join race 
		right join (
			-- first, get the best time for a runner by course and gender
			select runnerid, min(time) 'best_time'
			from result natural join competitor natural join runner 
				natural join gender natural join race race natural join course 
			where courseid=1 and genderid=2 and grade=12
			group by runnerid 
		) best on runner.runnerid=best.runnerid and result.time=best.best_time
	where courseid=1 and genderid=2 
	order by result.time
	limit 25
) t, 
(SELECT @rownum := 0) r;



-- GET TOP 15 TEAM TIMES FOR A **COURSE**/GENDER 
-- ** doesn't account for milliseconds
-- ** doesnt differentiate for runners from other divisions (ie, VB vs FSB)

-- fifth, add myrank number column
SELECT @rownum := @rownum + 1 AS myrank, t.* 
from (
	-- fourth, get the best time for each year and sort by best team time
	select yr as 'Year', 
		min(team_time) as 'Team Time',
		min(team_avg) as 'Avg. Ind. Time', 
		substring_index(group_concat(raceid order by team_time asc SEPARATOR "#"), "#", 1) as 'Race ID',
		substring_index(group_concat(competitors order by team_time asc SEPARATOR "#"), "#", 1) as 'Competitors'
	from (
		select year(date) yr, result.raceid, 
			SEC_TO_TIME(avg(TIME_TO_SEC(time))) as team_avg, 
			SEC_TO_TIME(sum(TIME_TO_SEC(time))) as team_time, 
			group_concat(competitorid order by time asc) as competitors
		from result natural join race inner join (
				-- second, order competitors for each race by fastest time
				select raceid, group_concat(concat(competitorid,":",raceid) order by time asc) as finisher_key 
				from result natural join race natural join competitor natural join runner 
				where genderid=2 and raceid in (
					select raceid 
					from (
						-- first, get races that have at least 5 results
						select raceid, count(raceid) as 'num_racers' 
						from result natural join race natural join competitor natural join runner 
						where courseid=1 and genderid=2
						group by raceid
					) num_racers_table
					where num_racers >= 5
				)
				group by raceid
			) finisher_tbl on result.raceid = finisher_tbl.raceid
			-- third, retrieve only the fastest 5 competitors for each race
			and find_in_set(concat(result.competitorid,":",result.raceid), finisher_tbl.finisher_key) between 1 and 5
		group by result.raceid
		order by yr,team_time
	) team_times 
	group by yr
	order by min(team_time)
	limit 15
) t, 
(SELECT @rownum := 0) r;


-- GET TOP 15 TEAM TIMES FOR A **RACE**/GENDER 
-- ** doesn't account for milliseconds
-- ** doesnt differentiate for runners from other divisions (ie, VB vs FSB)

SELECT @rownum := @rownum + 1 AS myrank, t.* 
from (
	-- fourth, get the best time for each year and sort by best team time
	select yr as 'Year', 
		min(team_time) as 'Team Time',
		min(team_avg) as 'Avg. Ind. Time', 
		min(team_pace) as 'Avg. Ind. Pace' 
	from (
		select year(date) yr, result.raceid, 
			SEC_TO_TIME(avg(TIME_TO_SEC(time))) as team_avg, 
			SEC_TO_TIME(avg(TIME_TO_SEC(pace))) as team_pace, 
			SEC_TO_TIME(sum(TIME_TO_SEC(time))) as team_time 
		from result natural join race inner join (
				-- second, order competitors for each race by fastest time
				select raceid, group_concat(concat(competitorid,":",raceid) order by pace asc) finisher_key 
				from result natural join race natural join competitor natural join runner 
				where genderid=2 and raceid in (
					select raceid 
					from (
						-- first, get races that have at least 5 results
						select raceid, count(raceid) as 'num_racers' 
						from result natural join race natural join competitor natural join runner 
						where genderid=2 and courseid in (
							select courseid from course where coursename like '%crystal%'
						)
						group by raceid
					) num_racers_table
					where num_racers >= 5
				)
				group by raceid
			) finisher_tbl on result.raceid = finisher_tbl.raceid
			-- third, retrieve only the fastest 5 competitors for each race
			and find_in_set(concat(result.competitorid,":",result.raceid), finisher_tbl.finisher_key) between 1 and 5
		group by result.raceid
		order by yr,team_time
	) team_times 
	group by yr
	order by min(team_pace)
	limit 15
) t, 
(SELECT @rownum := 0) r;



select * from course where coursename like '%half moon%';




-- , SEC_TO_TIME(avg(TIME_TO_SEC(time)))
select avg(time) as "Team Time" from (
select raceid,time,pace,grade,firstname,lastname,
	date,racename,coursename,coursedistance 
from result 
	natural join competitor natural join runner natural join gender natural join race 
	race natural join racename natural join racecondition natural join course natural join location natural join state natural join coursetype
where courseid=1 and genderid=3 and year=2007 and raceid in ('1000172')
order by time
limit 5
) test;







/*
Query Examples:
- results by:
	- athlete, ie "Ochoa", "Girmay"
	- course, ie "Crystal Springs", "Toro Park"
	- race name, ie "CCS", "League"
	- year, ie "2003", "2017"
	- gender, ie "male", "female"
	- grade, ie "9", "10", "11", "12"
- sort by:
	- pace
	- time
	- year
	- grade
	- date
	- first name
	- last name

*/
select * from racecondition order by raceconditionid;
select * from racename order by racenameid;
select * from coursetype order by coursetypeid;
select * from state order by stateid;

-- complete location details
select locationid,city,state from location natural join state order by locationid;

-- complete course details
select courseid,coursename,coursedistance,city,state,coursetype 
from course natural join location natural join state natural join coursetype 
order by courseid;

-- complete race details
select raceid,date,racename,racecondition,coursename,coursedistance,city,state,coursetype 
from race natural join racename natural join racecondition natural join course natural join location natural join state natural join coursetype 
order by raceid;

select * from gender order by genderid;

-- complete runner details
select runnerid,firstname,lastname,starthsxcyear,endhsxcyear,gender 
from runner natural join gender 
order by runnerid;

-- complete competitor details
select competitorid,year,grade,firstname,lastname,starthsxcyear,endhsxcyear,gender 
from competitor natural join runner natural join gender 
order by runnerid,grade;

-- complete result details
select competitorid,time,pace,year,grade,firstname,lastname,starthsxcyear,endhsxcyear,gender, 
	raceid,date,racename,racecondition,coursename,coursedistance,city,state,coursetype 
from result 
	natural join competitor natural join runner natural join gender natural join race 
	race natural join racename natural join racecondition natural join course natural join location natural join state natural join coursetype
order by runnerid,grade,raceid;

-- result details without extraneous info
select runnerid,time,pace,grade,firstname,lastname,
	date,racename,coursename,coursedistance 
from result 
	natural join competitor natural join runner natural join gender natural join race 
	race natural join racename natural join racecondition natural join course natural join location natural join state natural join coursetype
order by raceid,runnerid,grade,raceid;



SELECT table_schema AS "Database", 
ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS "Size (MB)" 
FROM information_schema.TABLES 
GROUP BY table_schema;


-- get all special achievements
SELECT `specialAchievementName`, `firstName`, `lastName`, `grade`, `year`, `notes`
FROM `SpecialAchiever` NATURAL JOIN `Competitor` NATURAL JOIN `SpecialAchievement` NATURAL JOIN `Runner` 
ORDER BY `year` DESC, `specialAchievementId` DESC;

-- league champions
SELECT `specialAchievementName`, `firstName`, `lastName`, `grade`, `year`, `notes`
FROM `SpecialAchiever` NATURAL JOIN `Competitor` NATURAL JOIN `SpecialAchievement` NATURAL JOIN `Runner` 
WHERE `specialAchievementId`=1
ORDER BY `year` DESC;

-- section champions
SELECT `specialAchievementName`, `firstName`, `lastName`, `grade`, `year`, `notes`
FROM `SpecialAchiever` NATURAL JOIN `Competitor` NATURAL JOIN `SpecialAchievement` NATURAL JOIN `Runner` 
WHERE `specialAchievementId`=2
ORDER BY `year` DESC;

-- state qualifiers
SELECT `specialAchievementName`, `firstName`, `lastName`, `grade`, `year`, `notes`
FROM `SpecialAchiever` NATURAL JOIN `Competitor` NATURAL JOIN `SpecialAchievement` NATURAL JOIN `Runner` 
WHERE `specialAchievementId`=3
ORDER BY `year` DESC, `notes` ASC;

