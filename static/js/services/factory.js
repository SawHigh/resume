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

app.factory('educations', ['$http', function($http) { 
  return $http.get('/sawhigh/api/education/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);

app.factory('worklogs', ['$http', function($http) { 
  return $http.get('/sawhigh/api/worllog/list/') 
            .success(function(data) { 	
              return data; 
            })  
}]);

app.service('fileUpload', ['$http', function ($http) {
    this.uploadFileToUrl = function(file, uploadUrl){
        var fd = new FormData();
        fd.append('avatar', file);
        $http.post(uploadUrl, fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        })
        .success(function(data){
          console.log(data);
        })
        .error(function(){
        });
    }
}]);