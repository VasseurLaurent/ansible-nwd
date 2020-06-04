(window.webpackJsonp=window.webpackJsonp||[]).push([[7],{353:function(e,a,t){"use strict";t.r(a);var r=t(43),v=Object(r.a)({},(function(){var e=this,a=e.$createElement,t=e._self._c||a;return t("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[t("h1",{attrs:{id:"default"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#default"}},[e._v("#")]),e._v(" Default")]),e._v(" "),t("p",[e._v("In the folder "),t("code",[e._v("default")]),e._v(" you can have two different patterns:")]),e._v(" "),t("ul",[t("li",[e._v("Default variables defined")]),e._v(" "),t("li",[e._v("Variables not defined by default but useful for your role")])]),e._v(" "),t("h2",{attrs:{id:"default-variables-defined"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#default-variables-defined"}},[e._v("#")]),e._v(" Default variables defined")]),e._v(" "),t("p",[e._v("If you define a default variable, they will be retrieved by "),t("code",[e._v("Ansible-nwd")]),e._v(" and their default values will be written in the documentation file.")]),e._v(" "),t("p",[e._v("Moreover, you can add information about these variables following this pattern:")]),e._v(" "),t("div",{staticClass:"language-yaml extra-class"},[t("pre",{pre:!0,attrs:{class:"language-yaml"}},[t("code",[t("span",{pre:!0,attrs:{class:"token key atrule"}},[e._v("your_variable")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v(":")]),e._v(" your_value "),t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# description of your variable;type")]),e._v("\n")])])]),t("p",[e._v("For example :")]),e._v(" "),t("div",{staticClass:"language-yaml extra-class"},[t("pre",{pre:!0,attrs:{class:"language-yaml"}},[t("code",[t("span",{pre:!0,attrs:{class:"token key atrule"}},[e._v("default_variable1")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v(":")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token number"}},[e._v("1.8")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# default variable1 version;number")]),e._v("\n"),t("span",{pre:!0,attrs:{class:"token key atrule"}},[e._v("default_variable2")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v(":")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token number"}},[e._v("2.7")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# default variable2 version;number")]),e._v("\n"),t("span",{pre:!0,attrs:{class:"token key atrule"}},[e._v("other_variable")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v(":")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token number"}},[e._v("3.4")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# other variable version;number")]),e._v("\n"),t("span",{pre:!0,attrs:{class:"token key atrule"}},[e._v("test")]),t("span",{pre:!0,attrs:{class:"token punctuation"}},[e._v(":")]),e._v(" "),t("span",{pre:!0,attrs:{class:"token number"}},[e._v("4.5")]),e._v("\n")])])]),t("p",[e._v("Will create this entry in your documentation file :")]),e._v(" "),t("table",[t("thead",[t("tr",[t("th",[e._v("Variable")]),e._v(" "),t("th",[e._v("Value")]),e._v(" "),t("th",[e._v("Description")]),e._v(" "),t("th",[e._v("Type")])])]),e._v(" "),t("tbody",[t("tr",[t("td",[t("code",[e._v("default_variable1")])]),e._v(" "),t("td",[e._v("1.8")]),e._v(" "),t("td",[e._v("default variable1 version")]),e._v(" "),t("td",[e._v("number")])]),e._v(" "),t("tr",[t("td",[t("code",[e._v("default_variable2")])]),e._v(" "),t("td",[e._v("2.7")]),e._v(" "),t("td",[e._v("default variable2 version")]),e._v(" "),t("td",[e._v("number")])]),e._v(" "),t("tr",[t("td",[t("code",[e._v("other_variable")])]),e._v(" "),t("td",[e._v("3.4")]),e._v(" "),t("td",[e._v("other variable version")]),e._v(" "),t("td",[e._v("number")])]),e._v(" "),t("tr",[t("td",[t("code",[e._v("test")])]),e._v(" "),t("td",[e._v("4.5")]),e._v(" "),t("td",[e._v("n/a")]),e._v(" "),t("td",[e._v("n/a")])])])]),e._v(" "),t("h2",{attrs:{id:"variables-not-defined-by-default"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#variables-not-defined-by-default"}},[e._v("#")]),e._v(" Variables not defined by default")]),e._v(" "),t("p",[e._v("There are some variables that you cannot define by default or not mandatory for your role.")]),e._v(" "),t("p",[e._v("With  "),t("code",[e._v("Ansible-nwd")]),e._v(" you can define some variables thank to tags in comment.")]),e._v(" "),t("p",[e._v("For example, if you want to specify a variable which is not defined as default you can do it following this pattern:")]),e._v(" "),t("div",{staticClass:"language-yaml extra-class"},[t("pre",{pre:!0,attrs:{class:"language-yaml"}},[t("code",[t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# @var variable;description;type;example;mandatory(bool)")]),e._v("\n")])])]),t("p",[e._v("For example :")]),e._v(" "),t("div",{staticClass:"language-yaml extra-class"},[t("pre",{pre:!0,attrs:{class:"language-yaml"}},[t("code",[t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# @var variable;variable description;type;example;false")]),e._v("\n"),t("span",{pre:!0,attrs:{class:"token comment"}},[e._v("# @var variable2;description2;type2;example2;true")]),e._v("\n")])])]),t("p",[e._v("Will create this entry in your documentation file :")]),e._v(" "),t("table",[t("thead",[t("tr",[t("th",[e._v("Variable")]),e._v(" "),t("th",[e._v("Type")]),e._v(" "),t("th",[e._v("Mandatory")]),e._v(" "),t("th",[e._v("Example")]),e._v(" "),t("th",[e._v("Description")])])]),e._v(" "),t("tbody",[t("tr",[t("td",[t("code",[e._v("variable")])]),e._v(" "),t("td",[e._v("type")]),e._v(" "),t("td",[e._v("false")]),e._v(" "),t("td",[e._v("example")]),e._v(" "),t("td",[e._v("variable description")])]),e._v(" "),t("tr",[t("td",[t("code",[e._v("variable2")])]),e._v(" "),t("td",[e._v("type2")]),e._v(" "),t("td",[e._v("true")]),e._v(" "),t("td",[e._v("example2")]),e._v(" "),t("td",[e._v("description2")])])])])])}),[],!1,null,null,null);a.default=v.exports}}]);