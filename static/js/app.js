  var csrftoken = function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

  var app = angular.module('resumeBackend', ['ngRoute','ngFileUpload', 'ngImgCrop']);

app.config(function ($routeProvider) { 
  $routeProvider 
    .when('/', { 
      templateUrl: '/static/templates/backend/home.html' 
    }) 
    .when('/profileUpdate/:edit', { 
      templateUrl: '/static/templates/backend/profile_update.html' 
    })
    .when('/create/:model', { 
      templateUrl: '/static/templates/backend/create.html' ,
      controller:'createCtrl'
    }) 
    .when('/update/:model/:id', { 
      templateUrl: '/static/templates/backend/update.html' ,
      controller:'updateCtrl'
    })    
    .otherwise({ 
      redirectTo: '/' 
    });
});

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
