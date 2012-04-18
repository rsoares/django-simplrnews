// Implementing WYMEDITOR for textareas.

(function($){
	$(document).ready(function() {
		$("textarea").wymeditor({
              containersHtml: '',
              classesHtml: '',
              logoHtml: '',
              toolsItems: [
                           {'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'},
                           {'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'},
                           {'name': 'Superscript', 'title': 'Superscript', 'css': 'wym_tools_superscript'},
                           {'name': 'Subscript', 'title': 'Subscript', 'css': 'wym_tools_subscript'},
                           {'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'},
                           {'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'},
                           {'name': 'CreateLink', 'title': 'Link', 'css': 'wym_tools_link'},
                           {'name': 'Unlink', 'title': 'Unlink', 'css': 'wym_tools_unlink'},
                           {'name': 'InsertImage', 'title': 'Image', 'css': 'wym_tools_image'},
                           {'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'},
                           {'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'},
                           {'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'},
                           ],
              updateEvent: "click",
              updateSelector: "input:submit"
      	});
	});
})(django.jQuery)	
