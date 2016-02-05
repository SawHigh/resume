app.controller('profileCtrl','$http', ['$scope', function($scope,$http) {
  $scope.profiles = {
      name:"",
      birthday:"",
      sexy:"",
      email:"",
      introducion:""
    }
    $scope.submit = function(){
      $http.post("/shop/shop_create/", $scope.profiles).success(function(data) {
           console.log(data);
        })
      
    };  
}]);