$(function(){

    
    $.ajax({
        url:"h0417/json/stu_score.json",
        data:"",
        type:"get",
        datatype:"json",
        success:function(data){
            console.log(data);
            s_count =data.length;
            let htmlData = "";
            for (let i=0; i<10; i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                htmlData += "<td>"+data[i].no+"</td>";
                htmlData += "<td>"+data[i].name+"</td>";
                htmlData += "<td>"+data[i].kor+"</td>";
                htmlData += "<td>"+data[i].eng+"</td>";
                htmlData += "<td>"+data[i].math+"</td>";
                htmlData += "<td>"+data[i].total+"</td>";
                htmlData += "<td>"+data[i].avg+"</td>";
                htmlData += "<td>"+data[i].rank+"</td>";
                htmlData += "<td><button class='delBtn'>삭제</td>";
                htmlData += "</tr>"
                
            }
            $("#body").html(htmlData);
        },
        error:function() { alert("애러"); }
    });
    
    //체크박스 전체 선택,취소>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            })
        }
    });
    
    //table 에 있는 삭제버튼 클릭>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    $(document).on("click",".delBtn",function(){
        console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제할래요??")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });
    //학생수정버튼 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    $("#modifyBtn").click(function(){
    console.log("체크박스에 표시된 개수 : "+$(".stuChk:checked").length);

    if($(".stuChk:checked").length >1){
        alert("학생 1명만 선택하셔야 수정이 됩니다");
        return false;
    }
    });//학생수정버튼















    //하단 삭제 버튼 클릭>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    $("#deleteBtn").click(function(){
        
        //체크되어있는것이 없을경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다");
            return false;
        }
        //현재 체크박스가 되어있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false;
        }
        //모든 체크박스 가져오기
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                console.log("현재 선택된 class 값 : "+$(this).val());
                console.log("현재 선택된 id 값 : "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });//each
    });//하단 삭제버튼
});//제이쿼리