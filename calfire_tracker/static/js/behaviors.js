jQuery(document).ready(function($) {



	// Sometimes RESOURCES DEPLOYED will publish "n/a" values
	// ============================================================
	$(".deployed dl").each(function(){
		var myResourceValue = $(this).find("dd");
		if(myResourceValue.text() == "n/a") {
			$(this).addClass("none");
		}
	});




	// Sometimes we won't have any UPDATES TRACKER posts
	// ============================================================
	if ($(".tertiaries .updates").length) {
		if ($(".tertiaries .updates article").length) {
			// do nothing; at least one has been published
		} else {
			$(".tertiaries .updates").remove();
			$(".tertiaries").addClass("just-the-facts").removeClass("clearfix");
		}
	}
	
	
	
	// Sometimes, "evacuations" text can just be too damn long.
	// ============================================================
	$(".fire-dashboard .damages .evacuations").each(function(){

		var evacsMax = 250;
		var myEvacsChars = $(this).find("dd").html().length;

		if(myEvacsChars > evacsMax) {
			$(".damages").addClass("spliced");
			$("<aside class=\"fire-message\"></aside>").insertAfter(".fire-dashboard");
			$(this).appendTo(".fire-message");
		}

	});




}); // end doc ready