$(function () {

    //侧边导航
    $(".lsm-sidebar-items").click(function () {
        $(this).find("a").addClass("active");
        $(this).siblings().find("a").removeClass("active");
        // $(".lsm-sidebar-itema").parent().removeClass("lsm-sidebar-show");
    })

    $(".lsm-sidebar-itemt").click(function () {
        $(this).find("a").addClass("active");
        $(this).siblings().find("a").removeClass("active");
    })

    $(".lsm-sidebar-itema").click(function () {
        $(".lsm-sidebar").find("a").removeClass("active");
    })

    $(".lsm-sidebar-item").click(function () {
        $(this).addClass("lsm-sidebar-show").siblings().removeClass("lsm-sidebar-show")
    })

    //首页待办事项切换
    $(".fk-statetab").click(function () {
        $(this).addClass("fk-statetabactive").siblings().removeClass("fk-statetabactive");
    })
    $('.fk-statetab').click(function (event) {
        $(this).addClass('fk-statetabactive');
        $(this).siblings().removeClass('fk-statetabactive');
        $('.fk-maintb .fk-handlingstatus').eq($(this).index()).addClass('fk-statusshow');
        $('.fk-maintb .fk-handlingstatus').eq($(this).index()).siblings().removeClass(
            'fk-statusshow');
    })

    //首页筛选screenMethod
    $(".fk-statusquerybtn").click(function () {
        $(this).parent().find(".fk-statusquerylists").addClass('active');
        $(".fk-statusquerybtn").find(".fk-querylistsicon").css("background-position",
            "-154px -102px");
        $(".fk-querylistcontauto").css("display", "block");
    })
    $(".fk-querylist").click(function () {
        var txt = $(this).text();
        $(this).parent().parent().siblings().find(".fk-statusquerytxt").text(txt);
        $(".fk-statusquerylists").removeClass('active');
        $(".fk-statusquerybtn").find(".fk-querylistsicon").css("background-position",
            "-140px -102px");
        $(".fk-querylistcontauto").hide();
    })

})