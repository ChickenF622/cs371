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

var lessPaths = ["./Less/*.less",
          "./Less/fuelux/fuelux.less",
          "./Less/bootstrap/bootstrap.less"
  ];

var jadePaths = ["./**/templates/jade/**/*.jade", "!./includes/jade/*.jade"
  ];

gulp.task("default", function()
    {
    });

gulp.task("test", function()
    {
      notify("Hello World!");
    });

gulp.task("add", function ()
    {
      return gulp.src(".")
        .on("error", function ()
            {
              console.log("No files to add");
            })
        .pipe(git.add());
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
                locals: {},
                pretty: true
              }))
        .on("error", errorNotification)
        .pipe(rename(function (path)
              {
                path.extname = ".cshtml";
                return path;
              }))
        .pipe(gulp.dest("./Views"));
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

