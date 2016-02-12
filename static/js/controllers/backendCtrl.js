var projectsModel = {
      inputFields:[
        {label:"title",inputType:"text"},
        {label:"condition",inputType:"select",values:[{label:"MOBILE",value:"mobile"},{label:"DESKTOP",value:"desktop"},{label:"BOTH",value:"both"}]},
        {label:"description",inputType:"textarea"},
        {label:"published_date",inputType:"text"},
        {label:"link",inputType:"text"},
        {label:"source_code",inputType:"text"}
        ],
        submitObject:{
            title:"",
            condition:"",
            description:"",
            published_date:"",
            link:"",
            source_code:""
      }
}

app.controller('profileCtrl', ['$scope','$http','$routeParams', 'profile',function($scope,$http,$routeParams,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data[0]; 
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
            alert(data.status);
           window.location = "#/";
        }) 
    }
}]);

app.controller('projectCtrl', ['$scope','$http', 'projects',function($scope,$http,projects) {
    projects.success(function(data) {
    $scope.projects = data.data; 
    console.log($scope.projects);
    });
    $scope.delete = function(id){
      var link = "/sawhigh/api/project/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
     location.reload();
   })} ;
}]);

app.controller('createCtrl',['$scope','$http','$routeParams',function($scope,$http,$routeParams){
    var currentModel = $routeParams.model;
    if(currentModel == "project"){
         var link = "/sawhigh/api/project/create/";
        $scope.inputs =  projectsModel.inputFields;
        $scope.create =  projectsModel.submitObject;
        };
$scope.submit= function(){
  console.log($scope.create);
  $http.post(link,$scope.create).success(function(data) {
    alert(data.status);
    window.location = "#/";
    location.reload();
  })
 };
}]);