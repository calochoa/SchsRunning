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

  $.fn.setDocTitle = function(fullName, year) {
    $(document).ready(function() {
      document.title = fullName + ' - ' + year + ' ' + document.title;
    });
  }

  $.fn.addToBreadcrumb = function(year, titleStr) {
    var seasonLink = $('<a>')
      .attr('href', '/santa-clara-high-track-and-field/season/' + year)
      .text(year + ' Season');
    $('.breadcrumb').append(seasonLink).append(' / ' + titleStr);
  }

  $.fn.setTitle = function(titleStr) {
    $('.text-muted').append(titleStr);
  }

  $.fn.setCareer = function(athleteId, fullName) {
    var athleteLink = $('<a>')
      .attr('href', '/santa-clara-high-track-and-field/athletes/' + athleteId)
      .text(fullName + ' (All Records)');
    $('.career').append(athleteLink);
  }

  $.fn.setHeaders = function(year) {
    $('.raceHeader').text(year + ' Season Best Track Times');
    $('.fieldHeader').text(year + ' Season Best Field Marks');
  }
