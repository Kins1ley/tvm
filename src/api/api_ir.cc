#include <tvm/expr.h>
#include <tvm/ir.h>
#include <ir/IROperator.h>
#include <tvm/api_registry.h>

namespace tvm {
namespace ir {
TVM_REGISTER_API("make.Add")
.set_body([](TVMArgs args,  TVMRetValue *ret) {
    Expr a = args[0], b = args[1];
    if (args.size() == 2) match_types_add_sub(a, b);
    else match_types(a, b);
    *ret = Add::make(a, b);
    });

}  // namespace ir
}  // namespace tvm