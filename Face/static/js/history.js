// JavaScript Document
// echarts
// create for AgnesXu at 20161115


//折线图
var line = echarts.init(document.getElementById('line1'));
var data1=['2.21','2.22','2.23','2.24','2.25','22.26','2.27','2.28','2.29','2.30','3.1','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','3.10','3.11','3.12','3.13','3.14','3.15','3.16','3.17','3.18','3.19','3.20'];
var data2=[44,23, 42, 18, 45, 48, 49,100,64,63,26,25,86,84,39,85,94,35,75,52,76,86,46,37,57,35,75,65,34,77];
var data=[];
data.push(data1);
data.push(data2);
line.setOption({
    color:["#32d2c9"],
    title: {
        x: 'left',
        text: '总分',
        textStyle: {
            fontSize: '15',
            color: '#4c4c4c',
            fontWeight: 'bolder'
        }
    },
    tooltip: {
        trigger: 'axis'
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
		rotate:45,
        data: data1,
        axisLabel: {
            interval:0
        }
    },
    yAxis: {
        type: 'value'
    },
	dataZoom: [
        {   // 这个dataZoom组件，默认控制x轴。
            type: 'inside', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
            start: 30,      // 左边在 10% 的位置。
            end: 100         // 右边在 60% 的位置。
        }
    ],
    series: [
        {
            name:'成绩',
            type:'line',
            data:data2,
            markLine: {data: [{type: 'average', name: '平均值'}]}
        }
    ]
}) ;



//柱状图
var pillar1 = echarts.init(document.getElementById('pillar1'));

pillar1.setOption({
    color:["#ce6e73","#ee804b","#ffc668"],
    title : {
        subtext: '平均分（分）'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        x: 'right',
        data:['您的班级','全市','全国']
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['语言','词汇','词汇1','词汇2','词汇3','词汇4',
            '词汇5','词汇6','词汇7','词汇8','词汇9','词汇10']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'您的班级',
            type:'bar',
            data:[74, 62, 56, 79, 80, 30, 55, 35, 38, 41, 75, 89]
        },
        {
            name:'全市',
            type:'bar',
            data:[70, 65, 80, 71, 70, 40, 35, 46, 58, 40, 56, 30]
        },
        {
            name:'全国',
            type:'bar',
            data:[60, 55, 70, 61, 60, 30, 45, 36, 48, 50, 56, 40]
        }
    ]
}) ;



//柱状图2
var pillar2 = echarts.init(document.getElementById('pillar2'));
pillar2.setOption({
    color:["#00afff"],
    tooltip : {
        trigger: 'axis'
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['语言','词汇','词汇1','词汇2','词汇3','词汇4',
            '词汇5','词汇6','词汇7']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'您的班级',
            type:'bar',
            data:[74, 62, 56, 79, 80, 30, 55, 35, 38]
        }
    ]
});
