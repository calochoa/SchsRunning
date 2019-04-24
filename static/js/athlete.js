  $.fn.addResults = function(eventId, results) {
    if ($.fn.isRaceResult(eventId)) {
      if ($('.raceResults').text() == 'No Track Times') {
        // remove placeholder text bc a race result will be appended
        $('.raceResults').text('');
      }
      $('.raceResults').append(results);
    } else if ($.fn.isFieldResult(eventId)) {
      if ($('.fieldResults').text() == 'No Field Marks') {
        // remove placeholder text bc a field result will be appended
        $('.fieldResults').text('');
      }
      $('.fieldResults').append(results);
    }
  }

  $.fn.setDocTitle = function(titleStr) {
    $(document).ready(function() {
      document.title = titleStr + ' - ' + document.title;
    });
  }

  $.fn.addToBreadcrumb = function(genderLinkStr, genderStr, titleStr) {
    var genderLink = $('<a>')
      .attr('href', '/santa-clara-high-track-and-field/athletes/' + genderLinkStr)
      .text(genderStr);
    $('.breadcrumb').append(genderLink).append(' / ' + titleStr);
  }

  $.fn.setTitle = function(titleStr) {
    $('.text-muted').text(titleStr);
  }

  $.fn.getGenderStr = function(genderId) {
    return (genderId == 2 ? 'Males' : 'Females');
  }

  $.fn.getGenderLinkStr = function(genderId) {
    return (genderId == 2 ? 'males' : 'females');
  }

  $.fn.getGradeStr = function(grade) {
    return (grade > 12 ? '' : ' (' + grade + ')');
  }

  $.fn.addPersonalRecord = function(prResults, year, grade, gradeStr) {
    var seasonLink = $('<a>')
      .attr('href', '/santa-clara-high-track-and-field/season/' + year)
      .attr('class', 'rankingsLink')
      .text(year + ' Season');
    var div = $('<div>').attr('class', 'seasonGrade').append('&raquo; ').append(seasonLink);
    if (grade <= 12) {
      div.append(' (' + gradeStr + ')');
    }
    $(prResults).find('p').prepend(div);
    $('.personalRecords').append(prResults); 
  }

  $.fn.addSeasonRecordsHeader = function(year, grade, gradeStr) {
    var seasonLink = $('<a>').attr('href', '/santa-clara-high-track-and-field/season/' + year).text(year + ' Season');
    var recordsHeader = $('<h4>').attr('class', 'recordsHeader');
    if (grade <= 12) {
      recordsHeader.append(gradeStr + '. Records - ');
    }
    recordsHeader.append(seasonLink);
    $('.seasonRecords').append(recordsHeader);
  }

  $.fn.addSeasonRecord = function(results) {
    $('.seasonRecords').append(results);
  }

