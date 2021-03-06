app.controller('userListCtrl', ['$rootScope','$scope','userList',function($rootScope,$scope,userList) {
    userList.success(function(data) {
    $scope.userLists = data.data; 
    $rootScope.title = "简历列表";
    }); 
}]);

app.controller('resumeCtrl', ['$rootScope','$scope','$http','$routeParams',function($rootScope,$scope,$http,$routeParams) {
    var id = $routeParams.id;
    $http.get('/sawhigh/api/profile/'+id+'/') 
            .success(function(data) { 	
              $scope.profile = data.data[0];
              $rootScope.title = data.data[0].name+'的简历';
              console.log($rootScope.title);
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