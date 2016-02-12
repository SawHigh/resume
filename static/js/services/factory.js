app.factory('profile', ['$http', function($http) { 
  return $http.get('/sawhigh/api/profile/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);

app.factory('projects', ['$http', function($http) { 
  return $http.get('/sawhigh/api/project/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);

app.factory('skills', ['$http', function($http) { 
  return $http.get('/sawhigh/api/skill/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);