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

app.directive('createField',function($compile) {
  return {
    restrict: 'A',
    replace: true,
    link:function(scope, element){
        var inputField = angular.element('<span>');
    switch(scope.input.inputType) {
          case 'textarea':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><textarea type="text" class="form-control" placeholder="'+scope.input.label+'"  ng-model="create.'+scope.input.label+'"/></div>');
            break;
          case 'text':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><input type="text" class="form-control" placeholder="'+scope.input.label+'" ng-model="create.'+scope.input.label+'"></div>');
            break;
            case 'select':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><select ng-options=" value.value as value.label for value in input.values" class="form-control" placeholder="'+scope.input.label+'" ng-model="create.'+scope.input.label+'"></div>');
            break;
            case 'date':
            inputField.append('<label  class="col-sm-4 control-label">{{input.label | uppercase}}</label><div class="col-sm-8"><input type="date" class="form-control" placeholder="'+scope.input.label+'" ng-model="create.'+scope.input.label+'"></div>');
            break;
    }  
    $compile(inputField)(scope);
    element.append(inputField);
    }
  }
});