USE `hsRunning`;



-- Test stored procedure (sp) calls
CALL `GetTopXcIndividual`(1,2,25);
CALL `GetCourseInfo`(25);
CALL `GetTopTeamCourse`(1,2,15);
CALL `GetXcRunnerResults`(1);
CALL `GetXcRunners`("2,3");
CALL `GetXcResultsByRaceCompetitor`("1000173,1000160,1000075,1000183,1000131,1000088,1000139,1000149,1000259,1000248,1000062,1000122,1000239,1000003,1000101",
"1000259.11,1000179.12,1000348.12,1000257.11,1000167.11,1000179.11,1000259.10,1000348.11,1000257.10,1000065.11,1000261.11,1000212.12,1000193.10,1000356.10,1000107.11,1000041.12,1000257.12,1000071.12,1000340.9,1000334.9,1000345.12,1000142.12,1.12,1000197.11,1000239.12,1000261.12,1000193.11,1000296.10,1000107.12,1000276.9,1000115.12,1000179.9,1000197.12,1000357.11,1000348.9,1000179.10,1000348.10,1000259.9,1000150.10,1000257.9,1000063.12,1000220.11,1000122.12,1000267.11,1000373.10,1000220.10,1000063.11,1000267.10,1000122.11,1000346.11,1000261.10,1000305.12,1000356.9,1000212.11,1000311.12,1.11,1000345.11,1000006.12,1000331.12,1000357.9,1000300.12,1000220.9,1000063.10,1000122.10,1000053.10,1000289.12,1000298.12,1000043.11,1000159.12,1000199.11,1000193.12,1000239.9,1000345.9,1000047.11,1.9");
CALL `GetXcCompetitorsByYear`(2003,2);
CALL `GetXcRacesByYear`(2003);
CALL `GetXcCompetitorResults`(1.12);
CALL `GetAllXcRaceResults`(1000131);
CALL `GetXcRaceResults`(1000131,2);
CALL `GetTopXcIndividualByGrade`(1,2,12,25);
CALL `GetCoachesByYear`(2018, "1,2");
CALL `GetCoachTimeline`("1,2");
CALL `GetCoachById`(1,"1,2");
CALL `GetCoaches`("1,2");
CALL `GetAwardsByYear`(2017,1);
CALL `GetAwardsById`("1,2","1,2,3,4",1);
CALL `GetAwardsTimeline`("2",1);
CALL `GetXcAlumniResultsByYear`(2017);
CALL `GetPastXcAlumniChampions`();
CALL `GetSpecialAchieversById`("1,2,3", 1);
-- Track & Field specific sp calls
CALL `GetTopTrackRaceIndividual`(1,3,15);
CALL `GetTopFieldIndividual`(29, 3, 20);
CALL `GetTopTrackRelayTeam`(25, 2, 20);
CALL `GetTrackCompetitorsByYear`(2018);
CALL `GetTrackEventsByYear`(2018);
CALL `GetTrackRaceResults`(1,2,2018);
CALL `GetTrackFieldResults`(29,1,2018);
CALL `GetTrackRelayResults`(25,1,2018);
CALL `GetTrackCompetitorResults`("1000464.12");
CALL `GetTrackAthletes`("3");
CALL `GetTrackAthleteResults`(1000464);
CALL `GetTrackRaceResultsByGrade`(8, 2, 12);
CALL `GetTrackFieldResultsByGrade`(29, 3, 9);
CALL `GetAllTrackRaceResults`(1, 3);
CALL `GetAllTrackFieldResults`(29, 2);
CALL `GetAllTrackRelayResults`(26, 3);
CALL `GetTrackRelayResultsBySquad`(25, 3, 1);


-- need to consider if i want to separate by course, ie ccs: Crystal vs Toro
-- or if i just want ORDER BY pace... discuss with Julie
USE `hsRunning`;
CALL `GetTopXcIndividualByRace`(3,3,0,0);
