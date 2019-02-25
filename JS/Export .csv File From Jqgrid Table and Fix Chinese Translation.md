### Export .csv File From Jqgrid Table and Fix Chinese Translation

##### What can this do

- Web : adding a download key and allowing downloading

- Export file: the exact table shown in website through jqGrid

##### Reference & Modification

- Refer : http://jsfiddle.net/hybrid13i/JXrwM/
- Modify
  - Using header columns form jqGrid instead of the json object. So that one could control the order of columns as well as adding translation like jqGrid does.
  -  Downloading inside of a blob object. This permits using non-English characters like Chinese

##### JS code (copy this directly)

```javascript
function JSONToCSVConvertor(JSONData, ReportTitle, IndexObject, Header) {
        /*
        Parameters:
            JSONData: Data of table stroed in a json object, or a string which could be parsed in to a json object. You may use the same data object used in jqGrid.
            ReprotTitle: Title of saved file
            IndexObject: use the colModel of jqGrid here to identify column order and their index.
            Header: use the colNames of jqGrid here to form a header of the file
        Returns (not necessary):
            0 : something goes wrong and the CSV is a empty string after computing
            1 : succeed in downloading
        */
    
        var arrData = typeof JSONData != 'object' ? JSON.parse(JSONData) : JSONData;
        var CSV = "";
		var row = "";
        // write header into the file
		for(head_idx in Header){
		    row += Header[head_idx] + ',';
		}
        row = row.slice(0, -1);
        CSV += row + '\r\n';
        // get index list
		var index_list = new Array();
		for(i=0; i<IndexObject.length; i++){
            index_list[i] = IndexObject[i].index
		}
        // write in content
        for (var i = 0; i < arrData.length; i++) {
            var row = "";
			var tmpArray = arrData[i];
            for (var index in index_list) {
				var prop = index_list[index];
                if(tmpArray.hasOwnProperty(prop)){
                    row += '"' + tmpArray[prop] + '",';
				}else{
                    row += '"",';
				}

            }
            row.slice(0, row.length - 1);
            CSV += row + '\r\n';
        }

        if (CSV == '') {
            alert("Invalid data");
            return 0;
        }

        // using blob obejct to fix the chinese issue
        var csv = '\ufeff' + CSV;
        var blob = new Blob([csv], { type: 'text/csv,charset=UTF-8' });

        // generate a file name
        var fileName = "Report_";
        //this will remove the blank-spaces from the title and replace it with an underscore
        fileName += ReportTitle.replace(/ /g,"_") + '.txt';
    
        // download
        if ('download' in document.createElement('a')) { // Non-IE
            var elink = document.createElement('a');
            elink.download = fileName;
            elink.style.display = 'none';
            elink.href = URL.createObjectURL(blob);
            document.body.appendChild(elink);
            elink.click();
            URL.revokeObjectURL(elink.href);
            document.body.removeChild(elink);
        } else { // IE10+
            navigator.msSaveBlob(blob, fileName);
        }
        // return
        return 1;
```



##### Example of calling

- Create a button

```html
<div align="right">
	<button id="download1" class='gen_btn'>DOWNLOAD</button>
</div>
```

- Collect column information from jqGrid

```javascript
function jqGrid(){
		var thHeader = ['日期(Date)','UID','OPENID','服务器(Zone)','渠道(Channel)'];
		var colModels = [
							{ name: 'date', index: 'date',align: 'center',frozen : true,width:80,sortable: true},
							{ name: 'uid', index: 'uid',align: 'center',frozen : true,width:140,sortable: true},
							{ name: 'openid', index: 'openid',align: 'center',frozen : false,width:140,sortable: true},
							{ name: 'zoneid', index: 'zoneid',align: 'center',frozen : false,width:140,sortable: true},
							{ name: 'channel', index: 'channel',align: 'center',frozen : false,width:140,sortable: true}},
	                    ];
	    var mydata = <%=tableJsonObject1%>;
	    $("#tableList1").jqGrid({
             datatype: 'local',
             data: mydata,
             caption : "日活跃用户信息全表",
             colNames: thHeader,
             colModel: colModels,
             rowNum: mydata.length,
             frozen: true,
             autowidth:false,
             sortname: 'date',
             sortorder: 'DESC',
             gridview: true,
             height: 580,
             width: 1200,
             autoScroll: true,
			 shrinkToFit: false,
			 viewrecords: false,
			 loadonce:true,
			 pgbuttons:false,
			 pginput:false,
             gridComplete: function() {
                 $("#gview_tableList").css({
                	 "margin-left": "auto",
                     "margin-right": "auto"
                 });
                 $("th div").css('font-weight','bold');
                 $("td[aria-describedby=tableList1_count]").css({
               	     "color":"green"
                });
             }
         });
		$("#tableList1").jqGrid('setFrozenColumns');

		// Need to define two global variable here 
		window.ColNames = thHeader;
		window.ColModel = colModels
	}
```

- Def button click and call the function

```javascript
    $(document).ready(function(){
        $("#download1").click(function(){
            var data = <%=tableJsonObject1%>; 
            if(data == '')
                return;
            JSONToCSVConvertor(data, "UserActiveExtend", ColModel, ColNames);
        });
    });
```

- CSS if needed

```html
<style>
		.gen_btn{
			padding:5px;
			background-color:#743ED9;
			color:white;
			font-family:arial;
			font-size:13px;
			border:2px solid black;
		}
		.gen_btn:hover{
			background-color:#9a64ff;
		}
</style>
```



