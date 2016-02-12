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
var skillsModel = {
      inputFields:[
        {label:"name",inputType:"text"},
        {label:"degree",inputType:"select",values:[{label:"了解",value:"1"},{label:"熟悉",value:"2"},{label:"掌握",value:"3"},{label:"精通",value:"4"},{label:"专家",value:"5"}]}
        ],
        submitObject:{
            name:"",
            degree:""
      }
}

var profileModel = {
      inputFields:[
        {label:"name",inputType:"text"},
        {label:"introducion",inputType:"textarea"},
        {label:"email",inputType:"text"},
        {label:"birthday",inputType:"text"},
        {label:"sex",inputType:"select",values:[{label:"Male",value:"Male"},{label:"Female",value:"Female"},{label:"Other",value:"Other"}]},
        {label:"phone",inputType:"text"},
        {label:"address",inputType:"text"}
        ],
        submitObject:{
            name:"",
            introducion:"",
            email:"",
            birthday:"",
            sex:"",
            phone:"",
            address:""
      }
}

app.controller('profileCtrl', ['$scope','$http', 'profile',function($scope,$http,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data[0]; 
    console.log($scope.profiles)
    }); 
}]);

app.controller('projectCtrl', ['$scope','$http', 'projects',function($scope,$http,projects) {
    projects.success(function(data) {
    $scope.projects = data.data; 
    });
    $scope.delete = function(id){
      var link = "/sawhigh/api/project/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
     location.reload();
   })} ;
}]);

app.controller('skillsCtrl', ['$scope','$http', 'skills',function($scope,$http,skills) {
    skills.success(function(data) {
    $scope.skills = data.data; 
    });
    $scope.delete = function(id){
      var link = "/sawhigh/api/skill/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
     location.reload();
   })} ;
}]);

app.controller('createCtrl',['$scope','$http','$routeParams',function($scope,$http,$routeParams){
    var currentModel = $routeParams.model;
    var link = "/sawhigh/api/"+currentModel+"/create/";
    switch(currentModel ){
      case 'project':
            $scope.inputs =  projectsModel.inputFields;
            $scope.inputValue =  projectsModel.submitObject;
     break;

     case 'skill':
            $scope.inputs =  skillsModel.inputFields;
            $scope.inputValue =  skillsModel.submitObject;
      break;
    }

$scope.submit= function(){
  $http.post(link,$scope.inputValue).success(function(data) {
    alert(data.status);
    window.location = "#/";
    location.reload();
  })
 };
}]);

app.controller('updateCtrl', ['$scope','$http','$routeParams',function($scope,$http,$routeParams) {
    var currentModel = $routeParams.model;
    var currentId = $routeParams.id;
    var listLink = "/sawhigh/api/"+currentModel+"/list/";
    $http.get(listLink) .success(function(data) {   
              $scope.inputValue  = data.data[currentId];
            })
    switch(currentModel ){
      case 'project':
            $scope.inputs =  projectsModel.inputFields;
     break;

     case 'skill':
            $scope.inputs =  skillsModel.inputFields;
      break;

      case 'profile':
            $scope.inputs =  $scope.inputs =  profileModel.inputFields;
      break;
    }
    $scope.submit = function(){
          var link = "/sawhigh/api/"+currentModel+"/"+$scope.inputValue.id+"/update/";
          var postJson =  $scope.inputValue;
          delete postJson.id;
          delete postJson.user_id;
          delete postJson.user;
          $http.post(link,postJson).success(function(data) {
            alert(data.status);
        }) 
          location.reload();
          window.location = "#/";

    }
}]);

app.controller('fileUpload', ['$scope', 'Upload', '$timeout', function ($scope, Upload, $timeout) {
    $scope.upload = function (dataUrl) {
        Upload.upload({
            url: '/sawhigh/api/profile/1/update/',
            avatar: {
                file: Upload.dataUrltoBlob(dataUrl)
            },
        }).then(function (response) {
            $timeout(function () {
                $scope.result = response.data;
            });
        }, function (response) {
            if (response.status > 0) $scope.errorMsg = response.status 
                + ': ' + response.data;
        }, function (evt) {
            $scope.progress = parseInt(100.0 * evt.loaded / evt.total);
        });
    }
}]);