var spreadsheetId = ''//←スプレッドシートのIDを入れる

//Postされたデータを受け取り
function doPost(e){
  var data = [      
    e.parameter.Date_Master, // マスター日時     
    e.parameter.Date, // 測定日時    
    e.parameter.Temperature, // 気温    
    e.parameter.Humidity, // 湿度   
    e.parameter.Brightness, //明るさ   
    new Date(), // アップロード終了時刻    
  ];
  //取得したデータをログに記載
  Logger.log(new Date());
  //スプレッドシートへのデータ行書き込み
  addData('sensor_data', data);
  return ContentService.createTextOutput("ok");
}

//スプレッドシートへのデータ行書き込み
function addData(sheetName, data){
  var sheet = SpreadsheetApp.openById(spreadsheetId).getSheetByName(sheetName);
  sheet.appendRow(data);
}
