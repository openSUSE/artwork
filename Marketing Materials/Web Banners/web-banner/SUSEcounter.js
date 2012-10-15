// 
//
// (c) 2008 Jakub Steiner <jimmac AT gmail.com>
//
//
// code & images redistributable under the GNU LGPL v2 or later
//
SUSECOUNTER = {
  daystogo: 0,
  message: 'days to go',
  days_remaining: function (date1,date2) {
    var dayinmiliseconds = 1000 * 60 * 60 * 24

    // Convert both dates to milliseconds
    var date1_ms = date1.getTime()
    var date2_ms = date2.getTime()

    var diffinms = date2_ms - date1_ms
    var diff = Math.round(diffinms/dayinmiliseconds)
    if (diff > 0) {
      return diff;
    } else {
      return 0;
    }
  },
  fadeInCounter: function () {
    var containerWidth = $('#countercontainer').width();
    $('#SUSEcounter').append("<div id='SUSEdaystogo'>" + SUSECOUNTER.daystogo + "</div>");
    $('#SUSEdaystogo')
    	.css({
    	  opacity: 0,
    		top: '-33%',
    		width: containerWidth
    	})
    	.animate({
    	  opacity: 1,
    	  top: '33%'
    	}, 200);
    $('#SUSEcounter').append("<div id='SUSEdays'>" + SUSECOUNTER.message + "</div>");
    $('#SUSEdays').hide().fadeIn(4000);
  },
  loadStylesheet: function (url) {
    $('head').append('<link rel="stylesheet" type="text/css" href="'+url+'" title="suse counter">');
  }
}


$(document).ready(function() {
  //console.log('foo');
  var prefix = ''; //base location of the script

  SUSECOUNTER.loadStylesheet('counter.css');
  var releasedate = new Date();
  releasedate.setFullYear(2010,06,15); //month - 1
  var today = new Date();
  SUSECOUNTER.daystogo = SUSECOUNTER.days_remaining(today,releasedate);
  //console.log(SUSECOUNTER.daystogo, today, releasedate)
  //var daystogo = 0;

  $('#nojavascriptlink').hide();
  $('#countercontainer').append("<div id='SUSEcounter'></div>");
  if (SUSECOUNTER.daystogo>0) {
    setTimeout(SUSECOUNTER.fadeInCounter, 2000);
  } else {
    //it's time, get it!
    $('#SUSEcounter').append("<a target='_parent' class='message' href='http://software.opensuse.org'>download here!</a>");
  }
});
