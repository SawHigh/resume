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
          console.log(profileUpdate);
          $http.post(link,profileUpdate).success(function(data) {
           console.log(data);
           window.location = "#/";
        }) 
    }
}]);