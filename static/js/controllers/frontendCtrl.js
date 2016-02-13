app.controller('userListCtrl', ['$scope','profile',function($scope,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data; 
    console.log($scope.profiles)
    }); 
}]);

app.controller('resumeCtrl', ['$scope','$http','$routeParams',function($scope,$http,$routeParams) {
    var id = $routeParams.id;
    $http.get('/sawhigh/api/profile/'+id+'/') 
            .success(function(data) { 	
              $scope.profile = data.data[0];
            })  

     $http.get('/sawhigh/api/skill/'+id+'/') 
            .success(function(data) { 	
              $scope.skills = data.data;
            })  

    $http.get('/sawhigh/api/project/'+id+'/') 
            .success(function(data) { 	
              $scope.projects = data.data;
              console.log($scope.projects);
            })
    $http.get('/sawhigh/api/worllog/'+id+'/') 
            .success(function(data) { 	
              $scope.worklogs = data.data;
            })  

    $http.get('/sawhigh/api/education/'+id+'/') 
            .success(function(data) { 	
              $scope.educations = data.data;
            })  


}]);