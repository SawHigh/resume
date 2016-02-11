app.controller('profileCtrl', ['$scope','$http','$routeParams', 'profile',function($scope,$http,$routeParams,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data[0]; 
    console.log($scope.profiles);
    }); 
    
    if($routeParams.edit == "edit"){
        $scope.readonly = false;
        $('#birth input').datepicker({
          format: "yyyy-mm-dd"
        });
    }else{
        $scope.readonly = true;
    };

    $scope.submit = function(){
          var link = "/sawhigh/api/profile/"+$scope.profiles.id+"/update/";
          var profileUpdate = {
            name:$scope.profiles.name,
            introducion:$scope.profiles.introducion,
            email:$scope.profiles.email,
            birthday:$scope.profiles.birthday,
            sex:$scope.profiles.sex,
            phone:$scope.profiles.phone,
            address:$scope.profiles.address
          };

          $http.post(link,profileUpdate).success(function(data) {
           window.location = "#/";
        }) 
    }
}]);

app.controller('createCtrl',['$scope','$http','$routeParams',function($scope,$http,$routeParams){
    var currentModel = $routeParams.model;
    if(currentModel == "project"){
         var link = "/sawhigh/api/project/create/";
        $scope.create = {
         title : "",
         condition : "",
          description : "",
         published_date : "",
         link : "",
        source_code : ""
        };
    }
    var getKey = Object.keys($scope.create);
    for (var i = getKey.length - 1; i >= 0; i--) {
      $('#createForm').prepend('<div class="form-group"><label class="col-sm-4 control-label">'+getKey[i].toUpperCase()+'</label><div class="col-sm-8"><input type="text" class="form-control" placeholder="'+getKey[i]+'" ng-model="create.'+getKey[i]+'"></div></div>'
        );
    };
$scope.create= function(){
  $http.post(link,$scope.create).success(function(data) {
    console.log($scope.create);
    window.location = "#/";
  })
};

}]);