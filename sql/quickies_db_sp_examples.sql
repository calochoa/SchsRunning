USE `quickies`;



CALL `GetAllExercises`();
CALL `GetExercises`("1,2,3,4,5,6", "bs0002");
CALL `GetExercises`("1", "bs0001,bs0002,bs0003,bs0004");
CALL `GetExercises`('1,2,3,4,5,6', 'bs0001,bs0002,bs0003,bs0004');
CALL `GetAllQuickies`();
CALL `GetQuickies`("1,2,3,4,5,6", "bs0002");
CALL `GetQuickies`("1", "bs0001,bs0002,bs0003,bs0004");
CALL `GetQuickies`('1,2,3,4,5', 'bs0001,bs0002,bs0003,bs0004');
CALL `GetQuickiesById`("q00012,q00010,q04008,q02012");
CALL `GetAllQuickieWorkouts`();
CALL `GetQuickieWorkouts`("1,2,3", "bs0002");
