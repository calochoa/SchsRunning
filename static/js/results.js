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