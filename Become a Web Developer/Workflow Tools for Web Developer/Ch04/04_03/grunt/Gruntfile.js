module.exports = function(grunt) {
  grunt.initConfig({
    // Loads the packages and dependencies
    pkg: grunt.file.readJSON('package.json'),
    
    // Sass task
    sass: {
      dist: {
        options: {                      
          style: 'compressed'
        },
        files: [{
          expand: true,
          cwd: 'sass',  // directory name
          src: ['*.scss'], // raw files for development
          dest: 'css', // destination output folder
          ext: '.css' // file extension
        }]
      }
    },
    // Watch task
    watch: {
      css: {
        files: '**/*.scss', // all files within the parent and its subfolders
        tasks: ['sass'] // run the 'sass' task defined above
      }
    }
  });
  
  // Load tasks
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks
  grunt.registerTask('default', ['watch']);
};