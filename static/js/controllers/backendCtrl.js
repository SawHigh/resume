app.controller('profileCtrl', ['$scope','$routeParams', 'profile',function($scope,$routeParams,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data[0]; 
    console.log($scope.profiles);
    }); 
    
    if($routeParams.edit == "edit"){
        $scope.readonly = false;
        $('#birth input').datepicker({});
    }else{
        $scope.readonly = true;
    };
}]);