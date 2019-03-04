DROP TABLE IF EXISTS `WorkoutOfTheDay`;
DROP TABLE IF EXISTS `Workouts`;
DROP TABLE IF EXISTS `QuickieOfTheDay`;
DROP TABLE IF EXISTS `OfTheDay`;
DROP TABLE IF EXISTS `Quickies`;
DROP TABLE IF EXISTS `QuickieTypes`;
DROP TABLE IF EXISTS `Exercises`;
DROP TABLE IF EXISTS `ExerciseTypes`;
DROP TABLE IF EXISTS `BodySplits`;



CREATE TABLE IF NOT EXISTS `BodySplits` (
    `bsId` VARCHAR(6) UNIQUE NOT NULL,
    `bsName` VARCHAR(255),
    `bsDescription` VARCHAR(255),
    `order` INT,
    
	PRIMARY KEY (`bsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `BodySplits` VALUES
    ('bs0000','All','One stop shop for all the quickies.',0),
    ('bs0001','Core','These quickies are intended to target your core and get you closer to attaining that 6 pack or toned tummy.',2),
    ('bs0002','Lower Body','Perform these quickies to focus on strengthening your lower body.',1),
    ('bs0003','Upper Body','Try these quickies if you want to improve your upper body.',3),
    ('bs0004','Total Body','Total body quickies are perfect for getting a complete workout and attaining an overall muscle balance.',4);



CREATE TABLE IF NOT EXISTS `ExerciseTypes` (
    `etId` VARCHAR(6) UNIQUE NOT NULL,
    `etName` VARCHAR(255),
    `etDescription` VARCHAR(255),
    `order` INT,
    
	PRIMARY KEY (`etId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `ExerciseTypes` VALUES
    ('et0000','All','These exercises require you to use your entire bodyweight.',1),
    ('et0001','Bar','These exercises require you to use your entire bodyweight.',2);



CREATE TABLE IF NOT EXISTS `Exercises` (
    `eId` VARCHAR(7) UNIQUE NOT NULL,
    `eName` VARCHAR(255),
    `eLevel` INT,
    `vId` VARCHAR(7),
    `bsId` VARCHAR(6),
    `etId` VARCHAR(6),
    
	PRIMARY KEY (`eId`),
	FOREIGN KEY (`bsId`) REFERENCES `BodySplits` (`bsId`),
	FOREIGN KEY (`etId`) REFERENCES `ExerciseTypes` (`etId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Exercises` VALUES
    ('e000001','front lever swings',6,'v000001','bs0001','et0001'),
    ('e000002','L sit pull-ups',5,'v000002','bs0000','et0001'),
    ('e000003','shoot-ups',2,'v000003','bs0001','et0000'),
    ('e000004','Spiderman push-ups',4,'v000004','bs0003','et0000'),
    ('e000005','clapping push-ups',5,'v000005','bs0003','et0000'),
    ('e000006','jumping chin-ups',3,'v000006','bs0003','et0001'),
    ('e000007','up down scissors',1,'v000007','bs0001','et0000'),
    ('e000008','chest-ups',3,'v000008','bs0001','et0000'),
    ('e000009','hanging knee raises',3,'v000009','bs0001','et0001'),
    ('e000010','sit-ups',3,'v000010','bs0001','et0000'),
    ('e000011','pistol squats',5,'v000011','bs0002','et0000'),
    ('e000012','hanging oblique raises',3,'v000012','bs0001','et0001'),
    ('e000013','high knees',1,'v000013','bs0002','et0000'),
    ('e000014','push-ups',3,'v000014','bs0003','et0000'),
    ('e000015','bicycle crunches',2,'v000015','bs0001','et0000'),
    ('e000016','side-to-side hops',1,'v000016','bs0002','et0000'),
    ('e000017','full-body crunches',3,'v000017','bs0001','et0000'),
    ('e000018','jumping pull-ups',3,'v000018','bs0003','et0001'),
    ('e000019','handstand push-ups',6,'v000019','bs0003','et0000'),
    ('e000020','single arm push-ups',6,'v000020','bs0003','et0000'),
    ('e000021','side crunches',1,'v000021','bs0001','et0000'),
    ('e000022','hanging hurdles',3,'v000022','bs0001','et0001'),
    ('e000023','commando pull-ups',4,'v000023','bs0003','et0001'),
    ('e000024','lunges',2,'v000024','bs0002','et0000'),
    ('e000025','calf raises',1,'v000025','bs0002','et0000'),
    ('e000026','hanging up down scissors',4,'v000026','bs0001','et0001'),
    ('e000027','jumping lunges',4,'v000027','bs0002','et0000'),
    ('e000028','leg raises',2,'v000028','bs0001','et0000'),
    ('e000029','incline push-ups',1,'v000029','bs0003','et0000'),
    ('e000030','burpee pull-ups',5,'v000030','bs0004','et0001'),
    ('e000031','dips',4,'v000031','bs0003','et0001'),
    ('e000032','seated dips',3,'v000032','bs0003','et0000'),
    ('e000033','four square hops',1,'v000033','bs0002','et0000'),
    ('e000034','clapping pull-ups',6,'v000034','bs0003','et0001'),
    ('e000035','box squats',2,'v000035','bs0002','et0000'),
    ('e000036','heiden hops',2,'v000036','bs0002','et0000'),
    ('e000037','inverted rows',3,'v000037','bs0003','et0001'),
    ('e000038','hanging leg raises',4,'v000038','bs0001','et0001'),
    ('e000039','burpees',4,'v000039','bs0004','et0000'),
    ('e000040','jumping jacks',1,'v000040','bs0004','et0000'),
    ('e000041','pull-ups',4,'v000041','bs0003','et0001'),
    ('e000042','behind the neck pull-ups',4,'v000042','bs0003','et0001'),
    ('e000043','crunches',1,'v000043','bs0001','et0000'),
    ('e000044','atomic tricep blasters',5,'v000044','bs0003','et0000'),
    ('e000045','forward backward hops',1,'v000045','bs0002','et0000'),
    ('e000046','squat jumps',3,'v000046','bs0002','et0000'),
    ('e000047','mountain climbers',2,'v000047','bs0004','et0000'),
    ('e000048','hanging leg rotations',4,'v000048','bs0001','et0001'),
    ('e000049','muscle-ups',6,'v000049','bs0003','et0001'),
    ('e000050','side-to-side pull-ups',5,'v000050','bs0003','et0001'),
    ('e000051','knee strikes',1,'v000051','bs0002','et0000'),
    ('e000052','chin-ups',4,'v000052','bs0003','et0001'),
    ('e000053','rolling sit-ups',1,'v000053','bs0001','et0000'),
    ('e000054','half wipers',3,'v000054','bs0001','et0000'),
    ('e000055','crunch kicks',1,'v000055','bs0001','et0000'),
    ('e000056','criss cross scissors',1,'v000056','bs0001','et0000'),
    ('e000057','open close scissors',1,'v000057','bs0001','et0000'),
    ('e000058','calf jumps',1,'v000058','bs0002','et0000'),
    ('e000059','wipers',4,'v000059','bs0001','et0000'),
    ('e000060','hanging criss cross scissors',4,'v000060','bs0001','et0001'),
    ('e000061','hanging open close scissors',4,'v000061','bs0001','et0001'),
    ('e000062','tuck jumps',4,'v000062','bs0002','et0000'),
    ('e000063','burpee tuck jumps',5,'v000063','bs0004','et0000'),
    ('e000064','burpee muscle-ups',6,'v000064','bs0004','et0001'),
    ('e000065','hanging shoot-ups',6,'v000065','bs0001','et0001'),
    ('e000066','hanging wipers',6,'v000066','bs0001','et0001'),
    ('e000067','decline push-ups',3,'v000067','bs0003','et0000'),
    ('e000068','plank jacks',2,'v000068','bs0004','et0000'),
    ('e100001','small arm circles',0,'v100001','bs0003','et0000'),
    ('e100002','reverse small arm circles',0,'v100002','bs0003','et0000'),
    ('e100003','large arm circles',0,'v100003','bs0003','et0000'),
    ('e100004','reverse large arm circles',0,'v100004','bs0003','et0000'),
    ('e100005','lateral arm raises',0,'v100005','bs0003','et0000'),
    ('e100006','front arm raises',0,'v100006','bs0003','et0000'),
    ('e100007','lateral rotator cuffs',0,'v100007','bs0003','et0000'),
    ('e100008','front rotator cuffs',0,'v100008','bs0003','et0000'),
    ('e100009','low arm criss crosses',0,'v100009','bs0003','et0000'),
    ('e100010','arm criss crosses',0,'v100010','bs0003','et0000'),
    ('e100011','high arm criss crosses',0,'v100011','bs0003','et0000'),
    ('e100012','running arm swings',0,'v100012','bs0003','et0000'),
    ('e100013','neck up-downs',0,'v100013','bs0003','et0000'),
    ('e100014','neck side-to-sides',0,'v100014','bs0003','et0000'),
    ('e100015','neck leans',0,'v100015','bs0003','et0000'),
    ('e100016','neck rotations',0,'v100016','bs0003','et0000'),
    ('e100017','heel-to-glutes',0,'v100017','bs0002','et0000'),
    ('e100018','knee hugs',0,'v100018','bs0002','et0000'),
    ('e100019','ankle hugs',0,'v100019','bs0002','et0000'),
    ('e100020','toe touches',0,'v100020','bs0002','et0000'),
    ('e100021','lateral leg swings',0,'v100021','bs0002','et0000'),
    ('e100022','front leg swings',0,'v100022','bs0002','et0000'),
    ('e100023','high hurdles',0,'v100023','bs0002','et0000'),
    ('e100024','reverse high hurdles',0,'v100024','bs0002','et0000');



CREATE TABLE IF NOT EXISTS `QuickieTypes` (
    `qtId` VARCHAR(6) UNIQUE NOT NULL,
    `qtName` VARCHAR(255),
    `qtDescription` VARCHAR(255),
    `order` INT,
    
	PRIMARY KEY (`qtId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `QuickieTypes` VALUES
    ('qt0001','Basic','Get in great shape by doing a combination of some or all of these quickies.',3),
    ('qt0002','Cardio','These quickies are the best way to get your feet moving and heart pumping.',4),
    ('qt0003','Junior','Try these beginner level quickies if you are just starting to work out.',2),
    ('qt0004','Power','Attempt these quickies if you enjoy an extremely difficult challenge.',6),
    ('qt0005','Bar','Bar Quickies are great if you want to challenge yourself with full body weight exercises.',5),
    ('qt0006','Ultimate','Give these quickies a whirl, if you''re a master of calisthenics.',7),
    ('qt0008','Stretching','Don''t forget to perform some dynamic stretches to get the blood flowing and loosen up your muscles before exercising.',1);



CREATE TABLE IF NOT EXISTS `Quickies` (
    `qId` VARCHAR(6) UNIQUE NOT NULL,
    `qtId` VARCHAR(6),
    `qDifficulty` INT,
    `bsId` VARCHAR(6),
    `qName` VARCHAR(255),
    `reps1` INT,
    `eId1` VARCHAR(7),
    `reps2` INT,
    `eId2` VARCHAR(7),
    `reps3` INT,
    `eId3` VARCHAR(7),
    `reps4` INT,
    `eId4` VARCHAR(7),
    
	PRIMARY KEY (`qId`),
	FOREIGN KEY (`qtId`) REFERENCES `QuickieTypes` (`qtId`),
	FOREIGN KEY (`bsId`) REFERENCES `BodySplits` (`bsId`),
	FOREIGN KEY (`eId1`) REFERENCES `Exercises` (`eId`),
	FOREIGN KEY (`eId2`) REFERENCES `Exercises` (`eId`),
	FOREIGN KEY (`eId3`) REFERENCES `Exercises` (`eId`),
	FOREIGN KEY (`eId4`) REFERENCES `Exercises` (`eId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Quickies` VALUES
    ('q00001','qt0003',1,'bs0001','Quick Core',10,'e000043',10,'e000021',10,'e000053',10,'e000028'),
    ('q00002','qt0003',1,'bs0001','Quick Pack',5,'e000054',10,'e000055',5,'e000053',10,'e000057'),
    ('q00003','qt0003',1,'bs0004','Quick Easy',5,'e000024',10,'e000029',15,'e000043',20,'e000040'),
    ('q00004','qt0003',1,'bs0004','Quick Start',15,'e000047',15,'e000007',15,'e000013',15,'e000025'),
    ('q00005','qt0003',1,'bs0002','Quick Burn',5,'e000024',10,'e000035',15,'e000058',20,'e000013'),
    ('q00006','qt0003',1,'bs0004','Quick Pump',10,'e000058',10,'e000035',10,'e000047',10,'e000029'),
    ('q00007','qt0003',1,'bs0003','Quick Silver',10,'e000032',20,'e000068',10,'e000029',20,'e000047'),
    ('q00008','qt0003',1,'bs0002','Quick Evo',10,'e000035',10,'e000025',10,'e000058',10,'e000046'),
    ('q00009','qt0003',1,'bs0003','Quick Up',10,'e000014',10,'e000068',10,'e000047',10,'e000029'),
    ('q00010','qt0003',1,'bs0004','Quick One',5,'e000014',10,'e000035',15,'e000056',20,'e000068'),
    ('q00011','qt0003',1,'bs0004','Quick Burst',15,'e000040',15,'e000013',15,'e000047',15,'e000068'),
    ('q00012','qt0003',1,'bs0004','Quick n Dirty',10,'e000053',10,'e000029',10,'e000035',10,'e000040'),
    ('q01001','qt0001',2,'bs0004','Bread & Butter',10,'e000024',20,'e000051',20,'e000017',10,'e000039'),
    ('q01002','qt0001',2,'bs0001','Core Galore',10,'e000054',15,'e000003',20,'e000055',25,'e000056'),
    ('q01003','qt0001',2,'bs0002','Heating Up',10,'e000046',15,'e000024',20,'e000035',25,'e000058'),
    ('q01004','qt0001',3,'bs0004','Boot Camp',10,'e000004',15,'e000044',20,'e000017',25,'e000003'),
    ('q01005','qt0001',3,'bs0001','Hard Core',25,'e000010',25,'e000028',25,'e000015',25,'e000017'),
    ('q01006','qt0001',4,'bs0003','Push-Up or Shut Up',10,'e000004',20,'e000067',20,'e000014',10,'e000005'),
    ('q01007','qt0001',4,'bs0003','Too Easy',10,'e000041',15,'e000044',20,'e000032',25,'e000067'),
    ('q01008','qt0001',3,'bs0004','BurpeEvo',15,'e000035',15,'e000014',15,'e000046',15,'e000039'),
    ('q01009','qt0001',2,'bs0001','Core Time',15,'e000007',15,'e000056',15,'e000057',15,'e000028'),
    ('q01010','qt0001',3,'bs0001','Ab Time',15,'e000017',30,'e000015',30,'e000028',15,'e000054'),
    ('q01011','qt0001',4,'bs0001','Six Pack',20,'e000054',40,'e000015',40,'e000007',20,'e000017'),
    ('q01012','qt0001',4,'bs0001','Harder Core',20,'e000008',40,'e000056',40,'e000054',20,'e000017'),
    ('q01013','qt0001',3,'bs0002','Up and Down',40,'e000025',20,'e000035',40,'e000058',20,'e000046'),
    ('q01014','qt0001',2,'bs0003','Shape Up',10,'e000014',20,'e000032',20,'e000068',10,'e000067'),
    ('q01015','qt0001',3,'bs0003','Step It Up',10,'e000039',20,'e000067',20,'e000047',10,'e000044'),
    ('q01016','qt0001',3,'bs0003','Do It Now',10,'e000004',20,'e000037',10,'e000031',20,'e000014'),
    ('q01017','qt0001',2,'bs0003','Nothing Special',10,'e000006',15,'e000014',20,'e000047',25,'e000029'),
    ('q02001','qt0002',2,'bs0002','Hip-Hop U Don''t Stop',10,'e000036',10,'e000045',10,'e000016',10,'e000033'),
    ('q02002','qt0002',2,'bs0004','Bang Bang Boogie',10,'e000036',20,'e000051',20,'e000047',10,'e000039'),
    ('q02003','qt0002',4,'bs0004','Beach Body',20,'e000047',40,'e000056',40,'e000015',20,'e000039'),
    ('q02004','qt0002',3,'bs0004','Go Hard',50,'e000013',10,'e000004',50,'e000015',10,'e000027'),
    ('q02005','qt0002',3,'bs0002','Hot In Here',30,'e000036',30,'e000051',10,'e000046',10,'e000027'),
    ('q02006','qt0002',4,'bs0002','Can''t Stop Won''t Stop',50,'e000058',20,'e000046',50,'e000013',20,'e000039'),
    ('q02007','qt0002',4,'bs0004','En Fuego',15,'e000004',40,'e000047',15,'e000039',40,'e000013'),
    ('q02008','qt0002',4,'bs0004','Evolution',10,'e000046',10,'e000041',10,'e000039',10,'e000030'),
    ('q02009','qt0002',4,'bs0002','Leg-endary',10,'e000062',20,'e000027',30,'e000036',40,'e000013'),
    ('q02010','qt0002',2,'bs0004','Mondays',20,'e000013',20,'e000036',20,'e000047',20,'e000007'),
    ('q02011','qt0002',2,'bs0004','24/7',15,'e000014',20,'e000007',15,'e000046',20,'e000040'),
    ('q02012','qt0002',2,'bs0004','Nap Time',15,'e000057',25,'e000015',15,'e000068',25,'e000040'),
    ('q02013','qt0002',2,'bs0004','I Got This',15,'e000014',25,'e000056',15,'e000035',25,'e000013'),
    ('q02014','qt0002',3,'bs0004','Muffin Tops',30,'e000051',10,'e000004',30,'e000015',10,'e000059'),
    ('q02015','qt0002',3,'bs0004','Wake Up',30,'e000013',30,'e000047',10,'e000062',10,'e000039'),
    ('q02016','qt0002',3,'bs0002','Jump Start',40,'e000040',30,'e000058',20,'e000046',10,'e000027'),
    ('q02017','qt0002',4,'bs0004','Some Day',10,'e000041',10,'e000039',10,'e000005',10,'e000063'),
    ('q03001','qt0005',1,'bs0004','Quick Bar Starzz',5,'e000006',10,'e000009',5,'e000018',10,'e000012'),
    ('q03002','qt0005',1,'bs0003','Quick Barz',5,'e000031',10,'e000037',15,'e000029',20,'e000009'),
    ('q03003','qt0005',2,'bs0003','Baby Cobra',5,'e000006',10,'e000018',5,'e000052',10,'e000037'),
    ('q03004','qt0005',3,'bs0001','Hang Time',15,'e000026',15,'e000060',15,'e000061',15,'e000038'),
    ('q03005','qt0005',3,'bs0001','Bar Core',10,'e000022',10,'e000038',10,'e000026',10,'e000048'),
    ('q03006','qt0005',4,'bs0003','Pull-Up or Shut Up',5,'e000041',5,'e000050',5,'e000042',5,'e000023'),
    ('q03007','qt0005',4,'bs0003','King Cobra',5,'e000034',10,'e000041',15,'e000052',20,'e000037'),
    ('q03008','qt0005',4,'bs0004','Bar Evolution',10,'e000009',10,'e000038',10,'e000041',10,'e000002'),
    ('q03009','qt0005',2,'bs0004','Hanging Around',5,'e000041',10,'e000037',15,'e000026',20,'e000009'),
    ('q03010','qt0005',4,'bs0004','Bar Fun',20,'e000031',20,'e000060',20,'e000041',20,'e000061'),
    ('q04001','qt0004',5,'bs0001','Power Pack',20,'e000059',30,'e000008',40,'e000017',50,'e000003'),
    ('q04002','qt0004',5,'bs0004','Turtle Power',15,'e000004',20,'e000039',25,'e000046',30,'e000059'),
    ('q04003','qt0004',5,'bs0004','Balance of Power',15,'e000030',20,'e000027',25,'e000044',30,'e000017'),
    ('q04004','qt0004',5,'bs0003','Power Up',20,'e000005',20,'e000004',20,'e000044',20,'e000031'),
    ('q04005','qt0004',5,'bs0004','Power Struggle',25,'e000041',25,'e000038',25,'e000039',25,'e000044'),
    ('q04006','qt0004',5,'bs0004','Rise to Power',30,'e000013',30,'e000005',30,'e000046',30,'e000039'),
    ('q04007','qt0004',5,'bs0004','Max Power',20,'e000041',30,'e000046',20,'e000004',30,'e000039'),
    ('q04008','qt0004',5,'bs0004','Power Evolution',30,'e000035',30,'e000039',30,'e000062',30,'e000063'),
    ('q04009','qt0004',5,'bs0001','Core Power',40,'e000008',50,'e000056',40,'e000003',50,'e000015'),
    ('q04010','qt0004',5,'bs0002','Power Burst',30,'e000046',50,'e000058',30,'e000062',50,'e000013'),
    ('q04011','qt0004',5,'bs0002','Powerful',25,'e000027',25,'e000036',25,'e000046',25,'e000063'),
    ('q04012','qt0004',5,'bs0003','Power Hitter',15,'e000034',20,'e000005',25,'e000031',30,'e000039'),
    ('q04013','qt0004',5,'bs0004','Absolute Power',20,'e000034',40,'e000017',20,'e000039',40,'e000062'),
    ('q04014','qt0004',5,'bs0004','Power Play',25,'e000036',25,'e000039',25,'e000004',25,'e000062'),
    ('q05001','qt0006',6,'bs0004','NOT Easy',10,'e000020',10,'e000019',10,'e000030',10,'e000011'),
    ('q05004','qt0006',6,'bs0004','Bar Starzz',10,'e000002',10,'e000001',10,'e000049',10,'e000034'),
    ('q05006','qt0006',6,'bs0001','Jungle Gym',10,'e000065',10,'e000066',10,'e000048',10,'e000001'),
    ('q05008','qt0006',6,'bs0004','Ultimate Evolution',10,'e000039',10,'e000030',10,'e000049',10,'e000064'),
    ('q06001','qt0008',0,'bs0003','Upper Stretchie #1',10,'e100001',10,'e100002',10,'e100003',10,'e100004'),
    ('q06002','qt0008',0,'bs0003','Upper Stretchie #2',10,'e100005',10,'e100006',10,'e100007',10,'e100008'),
    ('q06003','qt0008',0,'bs0003','Upper Stretchie #3',10,'e100009',10,'e100010',10,'e100011',10,'e100012'),
    ('q06004','qt0008',0,'bs0003','Upper Stretchie #4',10,'e100013',10,'e100014',10,'e100015',10,'e100016'),
    ('q06005','qt0008',0,'bs0002','Lower Stretchie #1',10,'e100017',10,'e100018',10,'e100019',10,'e100020'),
    ('q06006','qt0008',0,'bs0002','Lower Stretchie #2',10,'e100021',10,'e100022',10,'e100023',10,'e100024');



CREATE TABLE IF NOT EXISTS `OfTheDay` (
    `otdId` VARCHAR(7) UNIQUE NOT NULL,
    `otdName` VARCHAR(255),
    `otdAbbr` VARCHAR(15),
    `order` INT,
    
	PRIMARY KEY (`otdId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `OfTheDay` VALUES
    ('otd0000','All','All',0),
    ('otd0001','Level 1','1',1),
    ('otd0002','Level 2','2',2),
    ('otd0003','Level 3','3',3),
    ('otd0004','Level 4','4',4),
    ('otd0005','Level 5','5',5);



CREATE TABLE IF NOT EXISTS `QuickieOfTheDay` (
    `otdId` VARCHAR(7) UNIQUE NOT NULL,
    `qotd_0_0` VARCHAR(6),
    `qotd_1_0` VARCHAR(6),
    `qotd_2_0` VARCHAR(6),
    `qotd_3_0` VARCHAR(6),
    `qotd_4_0` VARCHAR(6),
    `qotd_5_0` VARCHAR(6),
    `qotd_6_0` VARCHAR(6),
    `qotd_0_1` VARCHAR(6),
    `qotd_1_1` VARCHAR(6),
    `qotd_2_1` VARCHAR(6),
    `qotd_3_1` VARCHAR(6),
    `qotd_4_1` VARCHAR(6),
    `qotd_5_1` VARCHAR(6),
    `qotd_6_1` VARCHAR(6),
    `order` INT,
    
	PRIMARY KEY (`otdId`),
	FOREIGN KEY (`otdId`) REFERENCES `OfTheDay` (`otdId`),
	FOREIGN KEY (`qotd_0_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_1_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_2_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_3_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_4_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_5_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_6_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_0_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_1_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_2_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_3_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_4_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_5_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_6_1`) REFERENCES `Quickies` (`qId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `QuickieOfTheDay` VALUES
    ('otd0001','q03002','q00004','q00007','q00005','q00001','q00003','q00006','q03001','q00011','q00009','q00008','q00002','q00012','q00010',1),
    ('otd0002','q03003','q02002','q01017','q01003','q01002','q01001','q02011','q03009','q02010','q01014','q02001','q01009','q02012','q02013',2),
    ('otd0003','q03005','q02016','q01016','q02005','q01005','q01004','q02004','q03004','q01008','q01015','q01013','q01010','q02014','q02015',3),
    ('otd0004','q03007','q02007','q01007','q02006','q01012','q03008','q02008','q03006','q02003','q01006','q02009','q01011','q03010','q02017',4),
    ('otd0005','q04003','q04002','q04012','q04010','q04009','q04007','q04006','q04005','q04008','q04004','q04011','q04001','q04013','q04014',5);



CREATE TABLE IF NOT EXISTS `WorkoutOfTheDay` (
    `otdId` VARCHAR(7) UNIQUE NOT NULL,
    `wotd_0` VARCHAR(5),
    `wotd_1` VARCHAR(5),
    `wotd_2` VARCHAR(5),
    `wotd_3` VARCHAR(5),
    `wotd_4` VARCHAR(5),
    `wotd_5` VARCHAR(5),
    `wotd_6` VARCHAR(5),
    `order` INT,
    
	PRIMARY KEY (`otdId`),
	FOREIGN KEY (`otdId`) REFERENCES `OfTheDay` (`otdId`),
	FOREIGN KEY (`wotd_0`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_1`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_2`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_3`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_4`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_5`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_6`) REFERENCES `Workouts` (`wId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `WorkoutOfTheDay` VALUES
    ('otd0001','w1007','w1001','w1002','w1003','w1004','w1005','w1006',1),
    ('otd0002','w2007','w2001','w2002','w2003','w2004','w2005','w2006',2),
    ('otd0003','w3007','w3001','w3002','w3003','w3004','w3005','w3006',3),
    ('otd0004','w4007','w4001','w4002','w4003','w4004','w4005','w4006',4),
    ('otd0005','w5007','w5001','w5002','w5003','w5004','w5005','w5006',5);
