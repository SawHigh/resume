app.factory('profile', ['$http', function($http) { 
  return $http.get('api/project/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);