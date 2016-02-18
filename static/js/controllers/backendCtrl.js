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
        {label:"degree",inputType:"select",values:[{label:"了解",value:"1"},{label:"掌握",value:"2"},{label:"熟悉",value:"3"},{label:"精通",value:"4"},{label:"专家",value:"5"}]}
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
        {label:"address",inputType:"text"},
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

var educationsModel = {
      inputFields:[
        {label:"title",inputType:"text"},
        {label:"start",inputType:"text"},
        {label:"end",inputType:"text"},
        ],
        submitObject:{
            title:"",
            start:"",
            end:""
      }
}

var worklogsModel = {
      inputFields:[
        {label:"job",inputType:"text"},
        {label:"company",inputType:"text"},
        {label:"start",inputType:"text"},
        {label:"end",inputType:"text"}
        ],
        submitObject:{
            job:"",
            company:"",
            start:"",
            end:""
      }
}

app.controller('profileCtrl', ['$scope','$http', 'profile',function($scope,$http,profile) {
    profile.success(function(data) {
    $scope.profiles = data.data[0]; 
    }); 
}]);

app.controller('projectCtrl', ['$scope','$http',function($scope,$http) {
     var projectsUpdate = function(){
      $http.get('/sawhigh/api/project/list/') 
            .success(function(data) {   
              $scope.projects = data.data;
            })  
          };
          projectsUpdate();
    $scope.delete = function(id){
      var link = "/sawhigh/api/project/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
    projectsUpdate();
   })} ;
}]);

app.controller('skillsCtrl', ['$scope','$http',function($scope,$http) {
    var skillsUpdate = function(){
      $http.get('/sawhigh/api/skill/list/') 
            .success(function(data) {   
              $scope.skills = data.data;
            })  
          };
      skillsUpdate();
    $scope.delete = function(id){
      var link = "/sawhigh/api/skill/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
    skillsUpdate();
   })} ;
}]);

app.controller('educationsCtrl', ['$scope','$http',function($scope,$http) {
    var educationsUpdate = function(){
      $http.get('/sawhigh/api/education/list/') 
            .success(function(data) {   
              $scope.educations = data.data;
            })  
          };
          educationsUpdate();
    $scope.delete = function(id){
      var link = "/sawhigh/api/education/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
   educationsUpdate();
   })} ;
}]);

app.controller('worklogsCtrl', ['$scope','$http',function($scope,$http) {
    var worklogsUpdate = function(){
      $http.get('/sawhigh/api/worllog/list/') 
            .success(function(data) {   
              $scope.worklogs = data.data;
            })  
          };
      worklogsUpdate();
    $scope.delete = function(id){
      var link = "/sawhigh/api/worllog/"+id+"/delete/";
     $http.post(link).success(function(data) {
    alert(data.status);
     worklogsUpdate();
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
            $scope.inputValue =  skillsModel.submitObject;
            $scope.inputs =  skillsModel.inputFields;
            
      break;
      case 'education':
            $scope.inputs =  educationsModel .inputFields;
            $scope.inputValue =  educationsModel .submitObject;
      break;

      case 'worllog':
            $scope.inputs =  worklogsModel .inputFields;
            $scope.inputValue =  worklogsModel .submitObject;
      break;
    }

$scope.submit= function(){
  $http.post(link,$scope.inputValue).success(function(data) {
    console.log($scope.inputValue);
    if(data.status == 'success'){
      alert(data.status);
      $http.get('/sawhigh/api/'+currentModel+'/list/') 
            .success(function(data) {   
              $scope[currentModel+'s'] = data.data;              
              window.location = "#/";
              location.reload();
            })  
    }else{
      alert(data.status+','+data.reason);
    }
    
           
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

       case 'education':
            $scope.inputs =   educationsModel .inputFields;
      break;
      case 'worllog':
            $scope.inputs =   worklogsModel .inputFields;
      break;
     
    }
    $scope.submit = function(){
          var link = "/sawhigh/api/"+currentModel+"/"+$scope.inputValue.id+"/update/";
          var postJson =  $scope.inputValue;
          delete postJson.id;
          delete postJson.user_id;
          delete postJson.user;
          $http.post(link,postJson).success(function(data) {
            if(data.status == 'success'){
              alert(data.status);
            $http.get('/sawhigh/api/'+currentModel+'/list/') 
            .success(function(data) {   
              $scope[currentModel+'s'] = data.data;
              console.log($scope[currentModel+'s'] );
              window.location = "#/";
            })
            }else{
              alert(data.status+','+data.reason);
            }            
        })
    }
}]);

app.controller('uploadCtrl', ['$scope', 'fileUpload', function($scope, fileUpload){
    
    $scope.uploadFile = function(id){
        var file = $scope.myFile;
        console.log('file is ' );
        console.dir(file);
        var uploadUrl = "/sawhigh/api/profile/avatar/"+id+"/update/";
        fileUpload.uploadFileToUrl(file, uploadUrl);
    };
    
}]);