
$(function(){
    
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ["Malory","Eddy","Donella","Roze","Lief","Byram","Kati","Olimpia","Isabeau","Leda"];
    let kor = [71,13,90,13,33,86,3,82,12,6];
    let eng = [8,38,46,34,65,86,46,42,69,14];
    let math = [3,15,54,73,81,79,82,86,52,3];
    let total = [82,66,120,179,256,228,226,218,133,23];
    let avg = [27,22,63,40,59,76,75,72,44,7];
    
    //tbody 부분 10개 행 생성
    let htmlData = "";

        //html소스를 tbody에 추가해준다
        $("#body").html(htmlData);

        //확인버튼
        $("#confirmBtn").click(function(){
        console.log("이름 : "+$("#name").val());
    
        let number = Math.max.apply(null,no)+1;
        let name = $("#name").val();
        let kor = $("#kor").val();
        let eng = $("#eng").val();
        let math = $("#math").val();
        let total= kor+eng+math;
        let avg = (total/3).toFixed(2); //소수점 2자리까지 반올림 출력
        let rank = 0;
        });

        //테이블에 tr추가
        for(let i=0; i<no.length; i++){
            htmlData +="<tr id='"+(i+1)+"'>";
            htmlData +="<td><input type='checkbox' name='stu' class='stuChk' value='"+(i+1)+"'></td>";
            htmlData +="<td>"+(i+1)+"</td>";
            htmlData +=`<td>${name[i]}</td>`;
            htmlData +=`<td>${kor[i]}</td>`;
            htmlData +=`<td>${eng[i]}</td>`;
            htmlData +=`<td>${math[i]}</td>`;
            htmlData +=`<td>${total[i]}</td>`;
            htmlData +=`<td>${avg[i]}</td>`;
            htmlData +="<td>0</td>";
            htmlData +="<td><button class='delBtn'>삭제</button></td>";
            htmlData +="</tr>";
        }
            //html소스를 tbody에 추가해준다
            $("#body").html(htmlData);

        //전체선택 체크
        $("#allChk").click(function(){
            if($(this).is(":checked")==true){
                //모든 체크박스 체크
                console.log(" 모두 체크되었습니다");
                $(".stuChk").each(function(){
                    $(this).prop("checked",true);
                })

            }else{
                //모든 체크박스 해제
                console.log(" 모두 해제되었습니다");
                $(".stuChk").each(function(){
                    $(this).prop("checked",false);
                })
            }//전체 체크
        })
        
        //테이블에 있는 오른쪽 삭제버튼
        $(".delBtn").click(function(){
            console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
            if(confirm("정말 삭제하시나요??")){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });
        
        //하단 삭제버튼 클릭
        $("#deleteBtn").click(function(){
            console.log("체크박스 개수 : "+$(".stuChk").length);
            console.log("체크박스에 체크된 개수 : "+$(".stuChk:checked").length);
            
            //체크 되어있는게 없을 경우
            if($(".stuChk:checked").length < 1){
                alert("삭제하려면 체크를 해야합니다");
                return false;
            }



            //현재 체크박스에서 체크가 되어있는지 확인하는거..
            if(!confirm("정말 삭제하시겠습니까?")){
                return false; //no버튼 클릭시 다시 돌아감
            }



            //모든 체크박스를 가져오기 여러가지 한번에 삭제하기
            $(".stuChk").each(function(){
                if($(this).is(":checked")==true){
                    console.log("현재 선택된 class값 : "+$(this).val());
                    $("#"+$(this).parent().parent().attr("id")).remove();
                }
            });//each



        });//jquery
});
