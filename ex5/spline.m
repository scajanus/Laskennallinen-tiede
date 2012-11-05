[x,y] = titanium;
plot(linspace(min(x),max(x)),csapi(x,y,linspace(min(x),max(x))))
hold on
plot(x,y,'r.')
xlim([min(x),max(x)])

f = csapi(x,y);
hold off
plot(linspace(min(x),max(x)),fnval( fnder(f), linspace(min(x),max(x))))
xlim([min(x),max(x)])