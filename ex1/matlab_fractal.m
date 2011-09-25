NITER = 100;
threshold = .00000001;
z1=1;
z2=-.5-0.86602540378443864676i;
z3=-.5+0.86602540378443864676i;

[xx,yy] = meshgrid(linspace(-1,1,1000), linspace(-1,1,1000));

solutions = xx(:) + 1i*yy(:);
select = 1:length(solutions);
niters = NITER*ones(numel(xx), 1);
which_root = zeros(numel(xx), 1);

for iteration = 1:NITER
 z = solutions(select);

 solutions(select) = z - ((z.^2).*z - 1) ./ (3*z.^2);

 differ = (z - solutions(select));
 converged = abs(differ) < threshold;
 problematic = isnan(differ);

 niters(select(converged)) = iteration;
 niters(select(problematic)) = NITER+1;
 select(converged | problematic) = []; % drop solved
end

which_root(abs(solutions-z1)<0.00001)=1;
which_root(abs(solutions-z2)<0.00001)=20;
which_root(abs(solutions-z3)<0.00001)=40;

niters = reshape(niters,size(xx));
solutions = reshape(which_root, size(xx));

image(solutions+niters./2.5) % for some extra colors
%based on: 
%http://quantombone.blogspot.com/2009/07/
%simple-newtons-method-fractal-code-in.html
