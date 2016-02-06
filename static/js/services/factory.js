app.factory('profile', ['$http', function($http) { 
  return $http.get('/sawhigh/api/profile/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);