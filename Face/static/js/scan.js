// JavaScript Document
// echarts
// create for AgnesXu at 20161115


//环状图 
var ring = echarts.init(document.getElementById('ring'));
var data1=20;
var data2=84;
var data3=86;
var value=[];
value.push(data1);
value.push(data2);
value.push(data3);
var labelTop = {
    normal : {
        label : {
            show : true,
            position : 'center',
            formatter : '{b}',
            textStyle: {
                baseline : 'bottom',
			    fontsize: '20'
            }
        },
        labelLine : {
            show : false
        }
    }
};

var labelFromatter = {
    normal : {
        label : {
            formatter : function (params){
                return 100 - params.value
            },
            textStyle: {
                baseline : 'top',
				fontSize:'20'
				
            }
        }
    },
}
var labelBottom = {
    normal : {
        color: '#ccc',
        label : {
            show : true,
            position : 'center'
        },
        labelLine : {
            show : false
        }
    },
    emphasis: {
        color: 'rgba(0,0,0,0)'
    }
};
var radius = [50, 65];
ring.setOption({
    color:["#33bb9f","#ffa259","#4cbbe6"],
    series : [
        {
            type : 'pie',
            center : ['15%', '58%'],
            radius : radius,
            x: '0%', // for funnel
            itemStyle : labelFromatter,
            data : [
                {name:'other', value:100-data1, itemStyle : labelBottom},
                {name:'年龄', value:data1,itemStyle : labelTop}
            ]
        },
        {
            type : 'pie',
            center : ['45%', '58%'],
            radius : radius,
            x:'20%', // for funnel
            itemStyle : labelFromatter,
            data : [
                {name:'other', value:100-data2, itemStyle : labelBottom},
                {name:'总分', value:data2,itemStyle : labelTop}
            ]
        },
        {
            type : 'pie',
            center : ['75%', '58%'],
            radius : radius,
            x:'40%', // for funnel
            itemStyle : labelFromatter,
            data : [
                {name:'other', value:100-data3, itemStyle : labelBottom},
                {name:'细腻度', value:data3,itemStyle : labelTop}
            ]
        }
    ]
}) ;

var ring = echarts.init(document.getElementById('ring1'));
var data4=74;
var data5=88;
var data6=85;
var value=[];
value.push(data4);
value.push(data5);
value.push(data6);
var labelTop = {
    normal : {
        label : {
            show : true,
            position : 'center',
            formatter : '{b}',
            textStyle: {
                baseline : 'bottom',
			    fontsize: '20'
            }
        },
        labelLine : {
            show : false
        }
    }
};

var labelFromatter = {
    normal : {
        label : {
            formatter : function (params){
                return 100 - params.value
            },
            textStyle: {
                baseline : 'top',
				fontSize:'20'
				
            }
        }
    },
}
var labelBottom = {
    normal : {
        color: '#ccc',
        label : {
            show : true,
            position : 'center'
        },
        labelLine : {
            show : false
        }
    },
    emphasis: {
        color: 'rgba(0,0,0,0)'
    }
};
var radius = [50, 65];
ring.setOption({
    color:["#ffb1bf","#a0abff","#00b384"],
    series : [
        {
            type : 'pie',
            center : ['15%', '58%'],
            radius : radius,
            x: '0%', // for funnel
            itemStyle : labelFromatter,
            data : [
                {name:'other', value:100-data4, itemStyle : labelBottom},
                {name:'年轻度', value:data1,itemStyle : labelTop}
            ]
        },
        {
            type : 'pie',
            center : ['45%', '58%'],
            radius : radius,
            x:'20%', // for funnel
            itemStyle : labelFromatter,
            data : [
                {name:'other', value:100-data5, itemStyle : labelBottom},
                {name:'健康度', value:data2,itemStyle : labelTop}
            ]
        },
        {
            type : 'pie',
            center : ['75%', '58%'],
            radius : radius,
            x:'40%', // for funnel
            itemStyle : labelFromatter,
            data : [
                {name:'other', value:100-data6, itemStyle : labelBottom},
                {name:'油干性', value:data3,itemStyle : labelTop}
            ]
        }
    ]
}) ;
window.onload=function(){
 "use strict";
  document.getElementsByid("wrinkle")[0].value=98;
};




