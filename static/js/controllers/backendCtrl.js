app.controller('profileCtrl', ['$scope', 'profile',function($scope,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data; 
    console.log($scope.profiles);
    }); 
}]);