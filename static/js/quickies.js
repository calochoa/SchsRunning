  $.fn.createQuickie = function(
    quickieName, reps1, exerciseName1, youTubeId1, reps2, exerciseName2, youTubeId2,
    reps3, exerciseName3, youTubeId3, reps4, exerciseName4, youTubeId4, levelName, bodySplit
  ) {
    return $('<div>').attr('class', 'quickieContainer')
      .append($('<div>').attr('class', 'quickie')
        .append($('<div>').attr('class', 'quickiesTitle').text(quickieName.toUpperCase()))
        .append($.fn.leftQuickieVideo(1, reps1, exerciseName1, youTubeId1))
        .append($.fn.rightQuickieVideo(2, reps2, exerciseName2, youTubeId2))
        .append($.fn.createClearDiv())
        .append($.fn.leftQuickieVideo(3, reps3, exerciseName3, youTubeId3))
        .append($.fn.rightQuickieVideo(4, reps4, exerciseName4, youTubeId4))
        .append($.fn.createClearDiv())
        .append($.fn.createQuickieInfo(levelName, bodySplit)));
  }

  $.fn.leftQuickieVideo = function(stepNo, reps, exerciseName, youTubeId) {
    return $('<div>').attr('class', 'leftQuickieVideo')
      .append($.fn.createStep(stepNo))
      .append($.fn.createRepExerciseName(reps, exerciseName))
      .append($.fn.createYouTubeVideo(youTubeId));
  }

  $.fn.rightQuickieVideo = function(stepNo, reps, exerciseName, youTubeId) {
    return $('<div>').attr('class', 'rightQuickieVideo')
      .append($.fn.createStep(stepNo))
      .append($.fn.createRepExerciseName(reps, exerciseName))
      .append($.fn.createYouTubeVideo(youTubeId));
  }

  $.fn.createStep = function(stepNo, repsExerciseName) {
    return $('<div>').attr('class', 'stepText').text('Step ' + stepNo);
  }

  $.fn.createRepExerciseName = function(reps, exerciseName) {
    return $('<div>').attr('class', 'repsExerciseName').text(reps + ' ' + exerciseName);
  }

  $.fn.createYouTubeVideo = function(youTubeId) {
    return $('<iframe>').attr('src', 'https://www.youtube.com/embed/' + youTubeId + '?rel=0&mute=1')
      .attr('width', '315').attr('height', '315').attr('frameborder', '0').attr('allowfullscreen', 'true');
  }

  $.fn.createClearDiv = function() {
    return $('<div>').attr('style', 'clear:both');
  }

  $.fn.createQuickieInfo = function(levelName, bodySplit) {
    return $('<div>').attr('class', 'quickieInfo').text(levelName + ' | ' + bodySplit);
  }

  $.fn.getLevelName = function(quickieLevel) {
    var levelName = 'Unknown';
    if (quickieLevel == 1) {
      levelName = 'Beginner';
    } else if (quickieLevel == 2) {
      levelName = 'Intermediate'
    } else if (quickieLevel == 3) {
      levelName = 'Advanced';
    } else if (quickieLevel == 4) {
      levelName = 'Expert';
    } else if (quickieLevel == 5 || quickieLevel == 6) {
      levelName = 'Master';
    }
    return levelName;
  }

  $.fn.addQuickie = function(quickie) {
    $('.quickies').append(quickie);
  }
