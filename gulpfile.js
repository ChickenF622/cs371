var gulp = require("gulp");
var git = require("gulp-git");
var jade = require("gulp-jade");
var less = require("gulp-less");
var minimist = require("minimist");
var notify = require("gulp-notify");
var path = require("path");
var rename = require("gulp-rename");

var errorNotification = notify.onError(function (error)
    {
      console.log(error.toString());
      return error.message;
    });

var lessPaths = ["**/static/*/css/less/*.less",
          "**/static/*/css/less/bootstrap/bootstrap.less"
  ];

var jadePaths = ["**/templates/*/jade/*.jade",
  ];

gulp.task("default", function()
    {
    });

gulp.task("less", function ()
    {
      return gulp.src(lessPaths)
        .pipe(less(
              {
                paths: [path.join(__dirname, "less", "includes")]
              }))
        .on("error", errorNotification)
        .pipe(gulp.dest("./Content"))
    });

gulp.task("jade", function ()
    {
      return gulp.src(jadePaths)
        .pipe(jade(
              {
                basedir: "C:\\Users\\Mark\\Google Drive\\School\\Notes\\CurrentYr\\CS371\\NobelPrize",
                locals: {},
                pretty: true
              }))
        .on("error", errorNotification)
        .pipe(rename(function (path)
              {
                path.dirname = path.dirname.replace("\\jade", "");
              })
            )
        .pipe(gulp.dest("."));
    });

var commitMessage =
{
  string: "msg",
  default: {msg: ""}
};
var commitOptions = minimist(process.argv.slice(2), commitMessage);
gulp.task("commit", ["add"], function ()
    {
      return gulp.src(".")
        .pipe(git.commit(commitOptions.msg));
    });

gulp.task("watch", function ()
    {
      var lessWatcher = gulp.watch("./Less/**/*.less", ["less"]);
      var jadeWatcher = gulp.watch(["./Jade/**/*.jade"], ["jade"]);
    });

