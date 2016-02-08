app.controller('profileCtrl', ['$scope', 'profile',function($scope,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data[0]; 
    console.log($scope.profiles);
    }); 
    $('#birth input').datepicker({});
}]);