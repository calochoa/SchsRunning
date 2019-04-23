  $.fn.getAbbrGradeName = function(grade) {
      var abbrGradeName = 'Unknown';
      if (grade ==  12) {
        abbrGradeName = 'Sr'
      } else if (grade ==  11) {
        abbrGradeName = 'Jr'
      } else if (grade ==  10) {
        abbrGradeName = 'So'
      } else if (grade ==  9) {
        abbrGradeName = 'Fr'
      }
      return abbrGradeName;
  }

  $.fn.getGradeName = function(grade) {
      var gradeName = 'All';
      if (grade ==  12) {
        gradeName = 'Senior'
      } else if (grade ==  11) {
        gradeName = 'Junior'
      } else if (grade ==  10) {
        gradeName = 'Sophomore'
      } else if (grade ==  9) {
        gradeName = 'Freshman'
      }
      return gradeName;
  }

  $.fn.getGenderName = function(genderId) {
    return genderId ==  3 ? ' Girls ' : ' Boys ';
  }

  $.fn.getSquadName = function(squadId) {
      var squadName = 'All';
      if (squadId ==  1) {
        squadName = 'Varsity'
      } else if (squadId ==  2) {
        squadName = 'Varsity'
      } else if (squadId ==  3) {
        squadName = 'Junior Varsity'
      } else if (squadId ==  4) {
        squadName = 'Frosh-Soph'
      }
      return squadName;
  }

  $.fn.getResultDiv = function(div, event, result, eventId, squadId, year, squad, squadRank, squadTotal, grade, genderId) {
    var results = $(div).clone();
    $(results).find('h4').append(
      $('<div>').attr('class', 'eventMark').append(event + ' - ' + result)
    );
    $(results).find('p').append(
      $.fn.getRankings(eventId, squadId, year, squad, squadRank, squadTotal, grade, genderId, allGradeRank, allGradeTotal, allTimeRank, allTimeTotal)
    );
    return results;
  }

  $.fn.getRankings = function(
    eventId, squadId, year, squad, squadRank, squadTotal, grade, genderId, allGradeRank, allGradeTotal, allTimeRank, allTimeTotal
  ) {
    var genderName = $.fn.getGenderName(genderId).trim();
    var seasonSquadRankDiv = $.fn.getSeasonSquadRankDiv(eventId, squadId, year, squad, squadRank, squadTotal);
    var allGradeRankDiv = $.fn.getAllGradeRankDiv(eventId, genderId, grade, genderName, allGradeRank, allGradeTotal);
    var allTimeRankDiv = $.fn.getAllTimeRankDiv(eventId, genderId, genderName, allTimeRank, allTimeTotal);
    var rankingsDiv = $('<div>').attr('class', 'rankings').append('Rankings');
    $(rankingsDiv).append(seasonSquadRankDiv).append(allGradeRankDiv).append(allTimeRankDiv);
    return rankingsDiv;
  }

  $.fn.getSeasonSquadRankDiv = function(eventId, squadId, year, squad, squadRank, squadTotal) {
    return $('<div>').append('&raquo; ')
      .append($('<a>')
        .attr('class', 'rankingsLink')
        .attr('href', '/santa-clara-high-track-and-field/results/' + eventId + '/' + squadId + '/' + year + '/')
        .append(year + ' ' + squad))
      .append(': ' + squadRank + ' of ' + squadTotal);
  }

  $.fn.getAllGradeRankDiv = function(eventId, genderId, grade, genderName, allGradeRank, allGradeTotal) {
    return $('<div>').append('&raquo; ')
      .append($('<a>')
        .attr('class', 'rankingsLink')
        .attr('href', '/santa-clara-high-track-and-field/events/' + eventId + '/' + genderId + '/' + grade)
        .append($.fn.getGradeName(grade) + ' ' + genderName))
      .append(': ' + allGradeRank + ' of ' + allGradeTotal);
  }

  $.fn.getAllTimeRankDiv = function(eventId, genderId, genderName, allTimeRank, allTimeTotal) {
    return $('<div>').append('&raquo; ')
      .append($('<a>')
        .attr('class', 'rankingsLink')
        .attr('href', '/santa-clara-high-track-and-field/events/' + eventId + '/' + genderId + '/0')
        .append($.fn.getGradeName(0) + ' ' + genderName))
      .append(': ' + allTimeRank + ' of ' + allTimeTotal);
  }

  $.fn.isRaceResult = function(eventId) {
    return (eventId >= 1 && eventId <= 28) || (eventId >= 38 && eventId <= 41);
  }

  $.fn.isFieldResult = function(eventId) {
    return (eventId >= 29 && eventId <= 37);
  }
