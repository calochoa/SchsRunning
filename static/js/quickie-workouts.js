  $.fn.getLevelName = function(workoutLevel) {
    var levelName = 'Unknown';
    if (workoutLevel == 1) {
      levelName = 'Beginner';
    } else if (workoutLevel == 2) {
      levelName = 'Intermediate'
    } else if (workoutLevel == 3) {
      levelName = 'Advanced';
    } else if (workoutLevel == 4) {
      levelName = 'Expert';
    } else if (workoutLevel == 5 || workoutLevel == 6) {
      levelName = 'Master';
    }
    return levelName;
  }

  $.fn.createQuickieWorkout = function(workoutName) {
    return $('<div>').attr('class', 'quickieWorkout')
      .append($('<div>').attr('class', 'workoutsTitle').text(workoutName.toUpperCase()));
  }

  $.fn.createQuickie = function(step, quickie) {
    var quickieLocation = step % 2 == 0 ? 'leftQuickie' : 'rightQuickie';
    return $('<div>').attr('class', quickieLocation)
      .append($.fn.createStepQuickieTitle(step + 1, quickie.QuickieName))
      .append($.fn.createRepsExercises(
        quickie.Reps1, quickie.ExerciseName1, quickie.Reps2, quickie.ExerciseName2, 
        quickie.Reps3, quickie.ExerciseName3, quickie.Reps4, quickie.ExerciseName4)
      );
  }

  $.fn.createStepQuickieTitle = function(step, quickieTitle) {
    return $('<div>').attr('class', 'stepQuickieTitleContainer')
      .append($('<span>').attr('class', 'stepText').text('Step ' + step + ':'))
            .append($('<span>').attr('class', 'quickiesTitle').text(quickieTitle));
  }

  $.fn.createRepsExercises = function(reps1, exercise1, reps2, exercise2, reps3, exercise3, reps4, exercise4) {
    return $('<ul>')
      .append($.fn.createRepExerciseName(reps1, exercise1))
      .append($.fn.createRepExerciseName(reps2, exercise2))
      .append($.fn.createRepExerciseName(reps3, exercise3))
      .append($.fn.createRepExerciseName(reps4, exercise4));
  }

  $.fn.createRepExerciseName = function(reps, exerciseName) {
    return $('<li>').attr('class', 'repsExercise').text(reps + ' ' + exerciseName);
  }

  $.fn.createQuickieWorkoutInfo = function(levelName, bodySplit) {
    return $('<div>').attr('class', 'quickieWorkoutInfo').text(levelName + ' | ' + bodySplit);
  }

  $.fn.createVideoViewLink = function(bodySplit, levelName, workoutName) {
    var bodySplitLink = bodySplit.toLowerCase().replace(' ', '-')+'/';
    var workoutLevelLink = levelName.toLowerCase()+'/';
    var workoutNameLink = workoutName.toLowerCase().replace(' ', '-');
    var videoViewLink = '/workouts/quickie-workouts/'+bodySplitLink+workoutLevelLink+workoutNameLink;
    return $('<div>').attr('class', 'videoViewLink')
      .append($('<a>').attr('href', videoViewLink).text('Video View'));
  }

  $.fn.addQuickieWorkout = function(quickieWorkout) {
    $('.quickieWorkouts').append(quickieWorkout);
  }
