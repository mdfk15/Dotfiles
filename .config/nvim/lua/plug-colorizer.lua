require'colorizer'.setup(
	{'*';},
	{
		RGB=true;
		RRGGBB=true;
		RRGGBBAA=true;
		names=true;
		mode='foreground'
	})
require'colorizer'.attach_to_buffer(0)
