// Loads the packages and dependencies
var gulp = require('gulp');
var sass = require('gulp-sass');

// Task for compiling Sass files
gulp.task('styles', function() {
  gulp.src('sass/*.scss')
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(gulp.dest('css'));
});

// Task for watching files
gulp.task('watch', function() {
  gulp.watch('sass/*.scss',['styles']);
});

// Run the tasks defined above
gulp.task('default', ['styles', 'watch']);



