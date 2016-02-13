var app = angular.module('resume', ['ngRoute']);

app.config(function ($routeProvider) { 
  $routeProvider 
    .when('/', { 
      templateUrl: '/static/templates/frontend/home.html' 
    }) 
    .when('/resume/:id', { 
      templateUrl: '/static/templates/frontend/resume.html' 
    })
    .otherwise({ 
      redirectTo: '/' 
    });
});