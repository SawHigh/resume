app.directive('profile',function() {
  return {
    restrict: 'E',
    templateUrl: '/static/js/directives/profile.html'
  };
});

app.directive('projects',function($routeParams) {
  return {
    restrict: 'E',
    templateUrl: '/static/js/directives/projects.html'
  };
});

app.directive('skills',function($routeParams) {
  return {
    restrict: 'E',
    templateUrl: '/static/js/directives/skills.html'
  };
});

app.directive('educations',function($routeParams) {
  return {
    restrict: 'E',
    templateUrl: '/static/js/directives/educations.html'
  };
});

app.directive('worklogs',function($routeParams) {
  return {
    restrict: 'E',
    templateUrl: '/static/js/directives/worklogs.html'
  };
});

app.directive('inputFields',function($compile) {
  return {
    restrict: 'A',
    replace: true,
    link:function(scope, element){
        var inputField = angular.element('<span>');
    switch(scope.input.inputType) {
          case 'textarea':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><textarea type="text" class="form-control" placeholder="'+scope.input.label+'"  ng-model="inputValue.'+scope.input.label+'"/></div>');
            break;
          case 'text':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><input type="text" class="form-control" placeholder="'+scope.input.label+'" ng-model="inputValue.'+scope.input.label+'"></div>');
            break;
            case 'select':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><select ng-options=" value.value as value.label for value in input.values" class="form-control" placeholder="'+scope.input.label+'" ng-model="inputValue.'+scope.input.label+'"></div>');
            break;
            case 'date':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><input type="date" class="form-control" placeholder="'+scope.input.label+'" ng-model="inputValue.'+scope.input.label+'"></div>');
            break;
            case 'file':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><input type="file" class="form-control" placeholder="'+scope.input.label+'" ng-model="inputValue.'+scope.input.label+'"></div>');
            break;
    }  
    $compile(inputField)(scope);
    element.append(inputField);
    }
  }
});

app.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;
            
            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);